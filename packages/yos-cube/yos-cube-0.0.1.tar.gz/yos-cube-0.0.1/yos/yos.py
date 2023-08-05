#!/usr/bin/env python

# Copyright (c) 2016 YOS Limited, All Rights Reserved
# SPDX-License-Identifier: Apache-2.0

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.

# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied.


# pylint: disable=too-many-arguments, too-many-locals, too-many-branches, too-many-lines, line-too-long,
# pylint: disable=too-many-nested-blocks, too-many-public-methods, too-many-instance-attributes, too-many-statements
# pylint: disable=invalid-name, missing-docstring, bad-continuation

import traceback
import sys
import re
import subprocess
import os
import contextlib
import shutil
import stat
import errno
import ctypes
from itertools import chain, izip, repeat
from urlparse import urlparse
import urllib2
import zipfile
import argparse
import tempfile
from distutils.version import LooseVersion


# Application version
ver = '0.0.1'

# Default paths to Mercurial and Git
hg_cmd = 'hg'
git_cmd = 'git'

ignores = [
    "make",
    "make.exe",
    "Makefile",
    "build",
    ".cproject",
    ".gdbinit",
    ".openocd_cfg",
    ".project",
    "yos",
    ".yos",
    ]

# reference to local (unpublished) repo - dir#rev
regex_local_ref = r'^([\w.+-][\w./+-]*?)/?(?:#(.*))?$'
# reference to repo - url#rev
regex_url_ref = r'^(.*/([\w.+-]+)(?:\.\w+)?)/?(?:#(.*?)?)?$'

# git url (no #rev)
regex_git_url = r'^(git\://|ssh\://|https?\://|)(([^/:@]+)(\:([^/:@]+))?@)?([^/:]+)[:/](.+?)(\.git|\/?)$'
# hg url (no #rev)
regex_hg_url = r'^(file|ssh|https?)://([^/:]+)/([^/]+)/?([^/]+?)?$'

# yos url is subset of hg. yos doesn't support ssh transport
regex_yos_url = r'^(https?)://([\w\-\.]*yos\.(co\.uk|org|com))/(users|teams)/([\w\-]{1,32})/(repos|code)/([\w\-]+)/?$'
# yos sdk builds url
regex_build_url = r'^(https?://([\w\-\.]*yos\.(co\.uk|org|com))/(users|teams)/([\w\-]{1,32})/(repos|code)/([\w\-]+))/builds/?([\w\-]{6,40}|tip)?/?$'

# base url for all yos related repos (used as sort of index)
yos_base_url = 'https://code.aliyun.com/yos'
# default YOS url
yos_os_url = 'https://code.aliyun.com/yos/yos.git'
# default yos component url
yos_lib_url = 'https://yos.org/users/yos_official/code/yos/builds/'
# yos SDK tools needed for programs based on yos SDK component
yos_sdk_tools_url = 'https://yos.org/users/yos_official/code/yos-sdk-tools'

# verbose logging
verbose = False
very_verbose = False
install_requirements = True
cache_repositories = True

# stores current working directory for recursive operations
cwd_root = ""

eclispe_project_dir = 'yos/makefiles/eclipse_project'

# Logging and output
def log(msg):
    sys.stdout.write(msg)
    sys.stdout.flush()

def message(msg):
    return "[yos] %s\n" % msg

def info(msg, level=1):
    if level <= 0 or verbose:
        for line in msg.splitlines():
            log(message(line))

def action(msg):
    for line in msg.splitlines():
        log(message(line))

def warning(msg):
    for line in msg.splitlines():
        sys.stderr.write("[yos] WARNING: %s\n" % line)
    sys.stderr.write("---\n")

def error(msg, code=-1):
    for line in msg.splitlines():
        sys.stderr.write("[yos] ERROR: %s\n" % line)
    sys.stderr.write("---\n")
    sys.exit(code)

def progress_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

progress_spinner = progress_cursor()

def progress():
    sys.stdout.write(progress_spinner.next())
    sys.stdout.flush()
    sys.stdout.write('\b')


# Process execution
class ProcessException(Exception):
    pass

def popen(command, stdin=None, **kwargs):
    # print for debugging
    info('Exec "'+' '.join(command)+'" in '+os.getcwd())
    try:
        proc = subprocess.Popen(command, **kwargs)
    except OSError as e:
        if e[0] == errno.ENOENT:
            error(
                "Could not execute \"%s\".\n"
                "Please verify that it's installed and accessible from your current path by executing \"%s\".\n" % (command[0], command[0]), e[0])
        else:
            raise e

    if proc.wait() != 0:
        raise ProcessException(proc.returncode, command[0], ' '.join(command), os.getcwd())

def pquery(command, stdin=None, **kwargs):
    if very_verbose:
        info('Query "'+' '.join(command)+'" in '+os.getcwd())
    try:
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, **kwargs)
    except OSError as e:
        if e[0] == errno.ENOENT:
            error(
                "Could not execute \"%s\".\n"
                "Please verify that it's installed and accessible from your current path by executing \"%s\".\n" % (command[0], command[0]), e[0])
        else:
            raise e

    stdout, _ = proc.communicate(stdin)

    if very_verbose:
        log(str(stdout).strip()+"\n")

    if proc.returncode != 0:
        raise ProcessException(proc.returncode, command[0], ' '.join(command), os.getcwd())

    return stdout

def rmtree_readonly(directory):
    def remove_readonly(func, path, _):
        os.chmod(path, stat.S_IWRITE)
        func(path)

    shutil.rmtree(directory, onerror=remove_readonly)


# Directory navigation
@contextlib.contextmanager
def cd(newdir):
    prevdir = os.getcwd()
    os.chdir(newdir)
    try:
        yield
    finally:
        os.chdir(prevdir)

def relpath(root, path):
    return path[len(root)+1:]


def staticclass(cls):
    for k, v in cls.__dict__.items():
        if hasattr(v, '__call__') and not k.startswith('__'):
            setattr(cls, k, staticmethod(v))

    return cls


# Handling for multiple version controls
scms = {}
def scm(name):
    def _scm(cls):
        scms[name] = cls()
        return cls
    return _scm

# pylint: disable=no-self-argument, no-method-argument, no-member, no-self-use, unused-argument
@scm('bld')
@staticclass
class Bld(object):
    name = 'bld'

    def isurl(url):
        m_url = re.match(regex_url_ref, url.strip().replace('\\', '/'))
        if m_url:
            return re.match(regex_build_url, m_url.group(1))
        else:
            return False

    def init(path):
        if not os.path.exists(path):
            os.mkdir(path)

    def cleanup():
        info("Cleaning up library build folder")
        for fl in os.listdir('.'):
            if not fl.startswith('.'):
                if os.path.isfile(fl):
                    os.remove(fl)
                else:
                    shutil.rmtree(fl)

    def clone(url, path=None, depth=None, protocol=None):
        m = Bld.isurl(url)
        if not m:
            raise ProcessException(1, "Not a library build URL")

        try:
            Bld.init(path)
            with cd(path):
                Bld.seturl(url+'/tip')
        except Exception as e:
            error(e[1], e[0])

    def fetch_rev(url, rev):
        rev_file = os.path.join('.'+Bld.name, '.rev-' + rev + '.zip')
        try:
            if not os.path.exists(rev_file):
                action("Downloading library build \"%s\" (might take a minute)" % rev)
                outfd = open(rev_file, 'wb')
                inurl = urllib2.urlopen(url)
                outfd.write(inurl.read())
                outfd.close()
        except:
            if os.path.isfile(rev_file):
                os.remove(rev_file)
            raise Exception(128, "Download failed!\nPlease try again later.")

    def unpack_rev(rev):
        rev_file = os.path.join('.'+Bld.name, '.rev-' + rev + '.zip')
        try:
            with zipfile.ZipFile(rev_file) as zf:
                action("Unpacking library build \"%s\" in \"%s\"" % (rev, os.getcwd()))
                zf.extractall('.')
        except:
            if os.path.isfile(rev_file):
                os.remove(rev_file)
            raise Exception(128, "An error occurred while unpacking library archive \"%s\" in \"%s\"" % (rev_file, os.getcwd()))

    def checkout(rev, clean=False):
        url = Bld.geturl()
        m = Bld.isurl(url)
        if not m:
            raise ProcessException(1, "Not a library build URL")
        rev = Hg.remoteid(m.group(1), rev)
        if not rev:
            error("Unable to fetch library build information")

        arch_url = m.group(1) + '/archive/' + rev + '.zip'
        Bld.fetch_rev(arch_url, rev)

        if rev != Bld.getrev() or clean:
            Bld.cleanup()

            info("Checkout \"%s\" in %s" % (rev, os.path.basename(os.getcwd())))
            try:
                Bld.unpack_rev(rev)
                Bld.seturl(url+'/'+rev)
            except Exception as e:
                error(e[1], e[0])

    def update(rev=None, clean=False, clean_files=False, is_local=False):
        return Bld.checkout(rev, clean)

    def untracked():
        return ""

    def seturl(url):
        info("Setting url to \"%s\" in %s" % (url, os.getcwd()))
        if not os.path.exists('.'+Bld.name):
            os.mkdir('.'+Bld.name)

        fl = os.path.join('.'+Bld.name, 'bldrc')
        try:
            with open(fl, 'w') as f:
                f.write(url)
        except IOError:
            error("Unable to write bldrc file in \"%s\"" % fl, 1)

    def geturl():
        with open(os.path.join('.bld', 'bldrc')) as f:
            url = f.read().strip()
        m = Bld.isurl(url)
        return m.group(1)+'/builds' if m else ''

    def getrev():
        with open(os.path.join('.bld', 'bldrc')) as f:
            url = f.read().strip()
        m = Bld.isurl(url)
        return m.group(8) if m else ''

    def getbranch():
        return "default"


# pylint: disable=no-self-argument, no-method-argument, no-member, no-self-use, unused-argument
@scm('hg')
@staticclass
class Hg(object):
    name = 'hg'
    ignore_file = os.path.join('.hg', 'hgignore')

    def isurl(url):
        '''
        m_url = re.match(regex_url_ref, url.strip().replace('\\', '/'))
        if m_url and not re.match(regex_build_url, m_url.group(1)):
            return re.match(regex_hg_url, m_url.group(1)) or re.match(regex_yos_url, m_url.group(1))
        else:
            return False
        '''
        return None

    def init(path=None):
        popen([hg_cmd, 'init'] + ([path] if path else []) + (['-v'] if very_verbose else ([] if verbose else ['-q'])))

    def cleanup():
        return True

    def clone(url, name=None, depth=None, protocol=None):
        popen([hg_cmd, 'clone', formaturl(url, protocol), name] + (['-v'] if very_verbose else ([] if verbose else ['-q'])))

    def add(dest):
        info("Adding reference \"%s\"" % dest)
        try:
            popen([hg_cmd, 'add', dest] + (['-v'] if very_verbose else ([] if verbose else ['-q'])))
        except ProcessException:
            pass

    def remove(dest):
        info("Removing reference \"%s\" " % dest)
        try:
            popen([hg_cmd, 'rm', '-f', dest] + (['-v'] if very_verbose else ([] if verbose else ['-q'])))
        except ProcessException:
            pass

    def commit(msg=None):
        popen([hg_cmd, 'commit'] + (['-m', msg] if msg else [])  + (['-v'] if very_verbose else ([] if verbose else ['-q'])))

    def publish(all_refs=None):
        popen([hg_cmd, 'push'] + (['--new-branch'] if all_refs else []) + (['-v'] if very_verbose else ([] if verbose else ['-q'])))

    def fetch():
        info("Fetching revisions from remote repository to \"%s\"" % os.path.basename(os.getcwd()))
        popen([hg_cmd, 'pull'] + (['-v'] if very_verbose else ([] if verbose else ['-q'])))

    def discard():
        info("Discarding local changes in \"%s\"" % os.path.basename(os.getcwd()))
        popen([hg_cmd, 'update', '-C'] + (['-v'] if very_verbose else ([] if verbose else ['-q'])))

    def checkout(rev, clean=False, clean_files=False):
        info("Checkout \"%s\" in %s" % (rev if rev else "latest", os.path.basename(os.getcwd())))
        if clean_files:
            files = pquery([hg_cmd, 'status', '--no-status', '-ui']).splitlines()
            for f in files:
                info("Remove untracked file \"%s\"" % f)
                os.remove(f)
        popen([hg_cmd, 'update'] + (['-C'] if clean else []) + (['-r', rev] if rev else []) + (['-v'] if very_verbose else ([] if verbose else ['-q'])))

    def update(rev=None, clean=False, clean_files=False, is_local=False):
        if not is_local:
            Hg.fetch()
        Hg.checkout(rev, clean, clean_files)

    def status():
        return pquery([hg_cmd, 'status'] + (['-v'] if very_verbose else ([] if verbose else ['-q'])))

    def dirty():
        return pquery([hg_cmd, 'status', '-q'])

    def untracked():
        return pquery([hg_cmd, 'status', '--no-status', '-u']).splitlines()

    def outgoing():
        try:
            pquery([hg_cmd, 'outgoing'])
            return 1
        except ProcessException as e:
            if e[0] != 1:
                raise e
            return 0

    def seturl(url):
        info("Setting url to \"%s\" in %s" % (url, os.getcwd()))
        hgrc = os.path.join('.hg', 'hgrc')
        tagpaths = '[paths]'
        remote = 'default'
        lines = []

        try:
            with open(hgrc) as f:
                lines = f.read().splitlines()
        except IOError:
            pass

        if tagpaths in lines:
            idx = lines.index(tagpaths)
            m = re.match(r'^([\w_]+)\s*=\s*(.*)$', lines[idx+1])
            if m:
                remote = m.group(1)
                del lines[idx+1]
            lines.insert(idx, remote+' = '+url)
        else:
            lines.append(tagpaths)
            lines.append(remote+' = '+url)

    def geturl():
        tagpaths = '[paths]'
        default_url = ''
        url = ''

        try:
            with open(os.path.join('.hg', 'hgrc')) as f:
                lines = f.read().splitlines()
                if tagpaths in lines:
                    idx = lines.index(tagpaths)
                    m = re.match(r'^([\w_]+)\s*=\s*(.*)$', lines[idx+1])
                    if m:
                        if m.group(1) == 'default':
                            default_url = m.group(2)
                        else:
                            url = m.group(2)
        except IOError:
            pass

        if default_url:
            url = default_url

        return formaturl(url or pquery([hg_cmd, 'paths', 'default']).strip())

    def getrev():
        if os.path.isfile(os.path.join('.hg', 'dirstate')):
            with open(os.path.join('.hg', 'dirstate'), 'rb') as f:
                return ''.join('%02x'%ord(i) for i in f.read(6))
        else:
            return ""

    def getbranch():
        return pquery([hg_cmd, 'branch']).strip() or ""

    def remoteid(url, rev=None):
        return pquery([hg_cmd, 'id', '--id', url] + (['-r', rev] if rev else [])).strip() or ""

    def hgrc():
        hook = 'ignore.local = .hg/hgignore'
        hgrc = os.path.join('.hg', 'hgrc')
        try:
            with open(hgrc) as f:
                exists = hook in f.read().splitlines()
        except IOError:
            exists = False

        if not exists:
            try:
                with open(hgrc, 'a') as f:
                    f.write('[ui]\n')
                    f.write(hook + '\n')
            except IOError:
                error("Unable to write hgrc file in \"%s\"" % hgrc, 1)

    def ignores():
        Hg.hgrc()
        try:
            with open(Hg.ignore_file, 'w') as f:
                f.write("syntax: glob\n"+'\n'.join(ignores)+'\n')
        except IOError:
            error("Unable to write ignore file in \"%s\"" % os.path.join(os.getcwd(), Hg.ignore_file), 1)

    def ignore(dest):
        Hg.hgrc()
        try:
            with open(Hg.ignore_file) as f:
                exists = dest in f.read().splitlines()
        except IOError:
            exists = False

        if not exists:
            try:
                with open(Hg.ignore_file, 'a') as f:
                    f.write(dest + '\n')
            except IOError:
                error("Unable to write ignore file in \"%s\"" % os.path.join(os.getcwd(), Hg.ignore_file), 1)

    def unignore(dest):
        Hg.ignore_file = os.path.join('.hg', 'hgignore')
        try:
            with open(Hg.ignore_file) as f:
                lines = f.read().splitlines()
        except IOError:
            lines = []

        if dest in lines:
            lines.remove(dest)
            try:
                with open(Hg.ignore_file, 'w') as f:
                    f.write('\n'.join(lines) + '\n')
            except IOError:
                error("Unable to write ignore file in \"%s\"" % os.path.join(os.getcwd(), Hg.ignore_file), 1)

# pylint: disable=no-self-argument, no-method-argument, no-member, no-self-use, unused-argument
@scm('git')
@staticclass
class Git(object):
    name = 'git'
    ignore_file = os.path.join('.git', 'info', 'exclude')

    def isurl(url):
        m_url = re.match(regex_url_ref, url.strip().replace('\\', '/'))
        if m_url and not re.match(regex_build_url, m_url.group(1)) and not re.match(regex_yos_url, m_url.group(1)):
            return re.match(regex_git_url, m_url.group(1))
        else:
            return False

    def init(path=None):
        popen([git_cmd, 'init'] + ([path] if path else []) + ([] if very_verbose else ['-q']))

    def cleanup():
        info("Cleaning up Git index")
        if os.path.exists(os.path.join('.git', 'logs')):
            rmtree_readonly(os.path.join('.git', 'logs'))

    def clone(url, name=None, depth=None, protocol=None):
        popen([git_cmd, 'clone', formaturl(url, protocol), name] + (['--depth', depth] if depth else []) + (['-v'] if very_verbose else ([] if verbose else ['-q'])))

    def add(dest):
        info("Adding reference "+dest)
        try:
            popen([git_cmd, 'add', dest] + (['-v'] if very_verbose else []))
        except ProcessException:
            pass

    def remove(dest):
        info("Removing reference "+dest)
        try:
            popen([git_cmd, 'rm', '-f', dest] + ([] if very_verbose else ['-q']))
        except ProcessException:
            pass

    def commit(msg=None):
        popen([git_cmd, 'commit', '-a'] + (['-m', msg] if msg else []) + (['-v'] if very_verbose else ([] if verbose else ['-q'])))

    def publish(all_refs=None):
        if all_refs:
            popen([git_cmd, 'push', '--all'] + (['-v'] if very_verbose else ([] if verbose else ['-q'])))
        else:
            remote = Git.getremote()
            branch = Git.getbranch()
            if remote and branch:
                popen([git_cmd, 'push', remote, branch] + (['-v'] if very_verbose else ([] if verbose else ['-q'])))
            else:
                err = "Unable to publish outgoing changes for \"%s\" in \"%s\".\n" % (os.path.basename(os.getcwd()), os.getcwd())
                if not remote:
                    error(err+"The local repository is not associated with a remote one.", 1)
                if not branch:
                    error(err+"Working set is not on a branch.", 1)

    def fetch():
        info("Fetching revisions from remote repository to \"%s\"" % os.path.basename(os.getcwd()))
        popen([git_cmd, 'fetch', '--all', '--tags'] + (['-v'] if very_verbose else ([] if verbose else ['-q'])))

    def discard(clean_files=False):
        info("Discarding local changes in \"%s\"" % os.path.basename(os.getcwd()))
        pquery([git_cmd, 'reset', 'HEAD'] + ([] if very_verbose else ['-q'])) # unmarks files for commit
        pquery([git_cmd, 'checkout', '.'] + ([] if very_verbose else ['-q'])) # undo  modified files
        pquery([git_cmd, 'clean', '-fd'] + (['-x'] if clean_files else []) + (['-q'] if very_verbose else ['-q'])) # cleans up untracked files and folders

    def merge(dest):
        info("Merging \"%s\" with \"%s\"" % (os.path.basename(os.getcwd()), dest))
        popen([git_cmd, 'merge', dest] + (['-v'] if very_verbose else ([] if verbose else ['-q'])))

    def checkout(rev, clean=False):
        if not rev:
            return
        info("Checkout \"%s\" in %s" % (rev, os.path.basename(os.getcwd())))
        branch = None
        refs = Git.getrefs(rev)
        for ref in refs: # re-associate with a local or remote branch (rev is the same)
            m = re.match(r'^(.*?)\/(.*?)$', ref)
            if m and m.group(2) != "HEAD": # matches origin/<branch> and isn't HEAD ref
                if not os.path.exists(os.path.join('.git', 'refs', 'heads', m.group(2))): # okay only if local branch with that name doesn't exist (git will checkout the origin/<branch> in that case)
                    branch = m.group(2)
            elif ref != "HEAD":
                branch = ref # matches local branch and isn't HEAD ref

            if branch:
                info("Revision \"%s\" matches a branch \"%s\" reference. Re-associating with branch" % (rev, branch))
                popen([git_cmd, 'checkout', branch] + ([] if very_verbose else ['-q']))
                break

        if not branch:
            popen([git_cmd, 'checkout', rev] + (['-f'] if clean else []) + ([] if very_verbose else ['-q']))

    def update(rev=None, clean=False, clean_files=False, is_local=False):
        if not is_local:
            Git.fetch()
        if clean:
            Git.discard(clean_files)
        if rev:
            Git.checkout(rev, clean)
        else:
            remote = Git.getremote()
            branch = Git.getbranch()
            if remote and branch:
                try:
                    Git.merge('%s/%s' % (remote, branch))
                except ProcessException:
                    pass
            else:
                err = "Unable to update \"%s\" in \"%s\"." % (os.path.basename(os.getcwd()), os.getcwd())
                if not remote:
                    info(err+" The local repository is not associated with a remote one.")
                if not branch:
                    info(err+" Working set is not on a branch.")

    def status():
        return pquery([git_cmd, 'status', '-s'] + (['-v'] if very_verbose else []))

    def dirty():
        return pquery([git_cmd, 'status', '-uno', '--porcelain'])

    def untracked():
        return pquery([git_cmd, 'ls-files', '--others', '--exclude-standard']).splitlines()

    def outgoing():
        # Get default remote
        remote = Git.getremote()
        if not remote:
            return -1
        # Get current branch
        branch = Git.getbranch()
        if not branch:
            # Default to "master" in detached mode
            branch = "master"
        try:
            # Check if remote branch exists
            if not pquery([git_cmd, 'rev-parse', '%s/%s' % (remote, branch)]):
                return 1
        except ProcessException:
            return 1
        # Check for outgoing commits for the same remote branch
        return 1 if pquery([git_cmd, 'log', '%s/%s..%s' % (remote, branch, branch)]) else 0

    # Checks whether current working tree is detached
    def isdetached():
        return True if Git.getbranch() == "" else False

    # Finds default remote
    def getremote():
        remote = None
        remotes = Git.getremotes('push')
        for r in remotes:
            remote = r[0]
            # Prefer origin which is Git's default remote when cloning
            if r[0] == "origin":
                break
        return remote

    # Finds all associated remotes for the specified remote type
    def getremotes(rtype='fetch'):
        result = []
        remotes = pquery([git_cmd, 'remote', '-v']).strip().splitlines()
        for remote in remotes:
            remote = re.split(r'\s', remote)
            t = re.sub('[()]', '', remote[2])
            if not rtype or rtype == t:
                result.append([remote[0], remote[1], t])
        return result

    def seturl(url):
        info("Setting url to \"%s\" in %s" % (url, os.getcwd()))
        return pquery([git_cmd, 'remote', 'set-url', 'origin', url]).strip()

    def geturl():
        url = ""
        remotes = Git.getremotes()
        for remote in remotes:
            url = remote[1]
            if remote[0] == "origin": # Prefer origin URL
                break
        return formaturl(url)

    def getrev():
        return pquery([git_cmd, 'rev-parse', 'HEAD']).strip()

    # Gets current branch or returns empty string if detached
    def getbranch(rev='HEAD'):
        try:
            branch = pquery([git_cmd, 'rev-parse', '--symbolic-full-name', '--abbrev-ref', rev]).strip()
        except ProcessException:
            branch = "master"
        return branch if branch != "HEAD" else ""

    # Finds refs (local or remote branches). Will match rev if specified
    def getrefs(rev=None, ret_rev=False):
        result = []
        lines = pquery([git_cmd, 'show-ref']).strip().splitlines()
        for line in lines:
            m = re.match(r'^(.+)\s+(.+)$', line)
            if m and (not rev or m.group(1).startswith(rev)):
                if re.match(r'refs\/(heads|remotes)\/', m.group(2)): # exclude tags
                    result.append(m.group(1) if ret_rev else re.sub(r'refs\/(heads|remotes)\/', '', m.group(2)))
        return result

    # Finds branches a rev belongs to
    def revbranches(rev):
        branches = []
        lines = pquery([git_cmd, 'branch', '-a', '--contains'] + ([rev] if rev else [])).strip().splitlines()
        for line in lines:
            if re.match(r'^\*?\s+\((.+)\)$', line):
                continue
            line = re.sub(r'\s+', '', line)
            branches.append(line)
        return branches

    def ignores():
        try:
            ignore_file_parent_directory = os.path.dirname(Git.ignore_file)
            if not os.path.exists(ignore_file_parent_directory):
                os.mkdir(ignore_file_parent_directory)

            with open(Git.ignore_file, 'w') as f:
                f.write('\n'.join(ignores)+'\n')
        except IOError:
            error("Unable to write ignore file in \"%s\"" % os.path.join(os.getcwd(), Git.ignore_file), 1)

    def ignore(dest):
        try:
            with open(Git.ignore_file) as f:
                exists = dest in f.read().splitlines()
        except IOError:
            exists = False

        if not exists:
            try:
                ignore_file_parent_directory = os.path.dirname(Git.ignore_file)
                if not os.path.exists(ignore_file_parent_directory):
                    os.mkdir(ignore_file_parent_directory)

                with open(Git.ignore_file, 'a') as f:
                    f.write(dest.replace("\\", "/") + '\n')
            except IOError:
                error("Unable to write ignore file in \"%s\"" % os.path.join(os.getcwd(), Git.ignore_file), 1)
    def unignore(dest):
        try:
            with open(Git.ignore_file) as f:
                lines = f.read().splitlines()
        except IOError:
            lines = []

        if dest in lines:
            lines.remove(dest)
            try:
                ignore_file_parent_directory = os.path.dirname(Git.ignore_file)
                if not os.path.exists(ignore_file_parent_directory):
                    os.mkdir(ignore_file_parent_directory)

                with open(Git.ignore_file, 'w') as f:
                    f.write('\n'.join(lines) + '\n')
            except IOError:
                error("Unable to write ignore file in \"%s\"" % os.path.join(os.getcwd(), Git.ignore_file), 1)

# Repository object
class Repo(object):
    is_local = False
    is_build = False
    name = None
    path = None
    url = None
    rev = None
    scm = None
    libs = []
    codes = []
    cache = None

    @classmethod
    def fromurl(cls, url, path=None):
        repo = cls()
        m_local = re.match(regex_local_ref, url.strip().replace('\\', '/'))
        m_repo_url = re.match(regex_url_ref, url.strip().replace('\\', '/'))
        m_bld_url = re.match(regex_build_url, url.strip().replace('\\', '/'))
        if m_local:
            repo.name = os.path.basename(path or m_local.group(1))
            repo.path = os.path.abspath(path or os.path.join(os.getcwd(), m_local.group(1)))
            repo.url = m_local.group(1)
            repo.rev = m_local.group(2)
            repo.is_local = True
        elif m_bld_url:
            repo.name = os.path.basename(path or m_bld_url.group(7))
            repo.path = os.path.abspath(path or os.path.join(os.getcwd(), repo.name))
            repo.url = m_bld_url.group(1)+'/builds'
            repo.rev = m_bld_url.group(8)
            repo.is_build = True
        elif m_repo_url:
            repo.name = os.path.basename(path or m_repo_url.group(2)[:-4])
            repo.path = os.path.abspath(path or os.path.join(os.getcwd(), repo.name))
            repo.url = formaturl(m_repo_url.group(1))
            repo.rev = m_repo_url.group(3)
            if repo.rev and repo.rev != 'latest' and not re.match(r'^([a-fA-F0-9]{6,40})$', repo.rev):
                error('Invalid revision (%s)' % repo.rev, -1)
        else:
            error('Invalid repository (%s)' % url.strip(), -1)

        cache_cfg = Global().get_cfg('CACHE', '')
        if cache_repositories and cache_cfg and cache_cfg != 'none' and cache_cfg != 'off' and cache_cfg != 'disabled':
            loc = cache_cfg if (cache_cfg and cache_cfg != 'on' and cache_cfg != 'enabled') else None
            repo.cache = loc or os.path.join(tempfile.gettempdir(), 'yos-repo-cache')

        return repo

    @classmethod
    def fromlib(cls, lib=None):
        with open(lib) as f:
            ref = f.read(200)

        m_local = re.match(regex_local_ref, ref.strip().replace('\\', '/'))
        m_repo_url = re.match(regex_url_ref, ref.strip().replace('\\', '/'))
        m_bld_url = re.match(regex_build_url, ref.strip().replace('\\', '/'))
        if not (m_local or m_bld_url or m_repo_url):
            warning(
                "File \"%s\" in \"%s\" uses a non-standard .comp or .codes file extension, which is not compatible with the yos build tools.\n" % (os.path.basename(lib), os.path.split(lib)[0]))
            return False
        else:
            return cls.fromurl(ref, lib[:lib.rfind('.')])

    @classmethod
    def fromcode(cls, code=None):
        with open(code) as f:
            ref = f.read(200)

        m_local = re.match(regex_local_ref, ref.strip().replace('\\', '/'))
        m_repo_url = re.match(regex_url_ref, ref.strip().replace('\\', '/'))
        m_bld_url = re.match(regex_build_url, ref.strip().replace('\\', '/'))
        if not (m_local or m_bld_url or m_repo_url):
            warning(
                "File \"%s\" in \"%s\" uses a non-standard .lib file extension, which is not compatible with the yos build tools.\n" % (os.path.basename(code), os.path.split(code)[0]))
            return False
        else:
            return cls.fromurl(ref, code[:code.rfind('.')])

    @classmethod
    def fromrepo(cls, path=None):
        repo = cls()
        if path is None:
            path = Repo.findparent(os.getcwd())
            if path is None:
                error(
                    "Could not find yos program in current path \"%s\".\n"
                    "You can fix this by calling \"yos new .\" or \"yos config root .\" in the root of your program." % os.getcwd())

        repo.path = os.path.abspath(path)
        repo.name = os.path.basename(repo.path)
        
        cache_cfg = Global().get_cfg('CACHE', '')
        if cache_repositories and cache_cfg and cache_cfg != 'none' and cache_cfg != 'off' and cache_cfg != 'disabled':
            loc = cache_cfg if (cache_cfg and cache_cfg != 'on' and cache_cfg != 'enabled') else None
            repo.cache = loc or os.path.join(tempfile.gettempdir(), 'yos-repo-cache')

        repo.sync()

        if repo.scm is None:
            warning(
                "Program \"%s\" in \"%s\" does not use source control management.\n"
                "To fix this you should use \"yos new .\" in the root of your program." % (repo.name, repo.path))

        return repo

    @classmethod
    def isrepo(cls, path=None):
        for name, _ in scms.items():
            if os.path.isdir(os.path.join(path, '.'+name)):
                return True

        return False

    @classmethod
    def findparent(cls, path=None):
        path = os.path.abspath(path or os.getcwd())

        while cd(path):
            if os.path.isfile(os.path.join(path, Cfg.file)) or Repo.isrepo(path):
                return path

            tpath = path
            path = os.path.split(path)[0]
            if tpath == path:
                break

        return None

    @classmethod
    def pathtype(cls, path=None):
        path = os.path.abspath(path or os.getcwd())

        depth = 0
        while cd(path):
            tpath = path
            path = Repo.findparent(path)
            if path:
                depth += 1
                path = os.path.split(path)[0]
                if tpath == path:       # Reached root.
                    break
            else:
                break

        return "directory" if depth == 0 else ("program" if depth == 1 else "library")

    @classmethod
    def revtype(cls, rev, ret_rev=False):
        if rev is None or len(rev) == 0:
            return 'latest' + (' revision in the current branch' if ret_rev else '')
        elif re.match(r'^([a-fA-F0-9]{6,40})$', rev) or re.match(r'^([0-9]+)$', rev):
            return 'rev' + (' #'+rev[0:12] if ret_rev else '')
        else:
            return 'branch' + (' '+rev if ret_rev else '')

    @classmethod
    def isurl(cls, url):
        m = re.match(regex_url_ref, url.strip().replace('\\', '/'))
        return True if m else False

    @property
    def lib(self):
        return self.path + '.' + ('bld' if self.is_build else 'component')

    @property
    def code(self):
        return self.path + '.' + ('bld' if self.is_build else 'codes')

    @property
    def fullurl(self):
        if self.url:
            return (self.url.rstrip('/') + '/' +
                    (('' if self.is_build else '#') +
                        self.rev if self.rev else ''))

    def sync(self):
        self.url = None
        self.rev = None
        if os.path.isdir(self.path):
            try:
                self.scm = self.getscm()
                if self.scm and self.scm.name == 'bld':
                    self.is_build = True
            except ProcessException:
                pass

            try:
                self.url = self.geturl()
                if not self.url:
                    self.is_local = True
                    ppath = self.findparent(os.path.split(self.path)[0])
                    self.url = relpath(ppath, self.path).replace("\\", "/") if ppath else os.path.basename(self.path)
            except ProcessException:
                pass

            try:
                self.rev = self.getrev()
            except ProcessException:
                pass

            try:
                self.libs = list(self.getlibs())
            except ProcessException:
                pass

            try:
                self.codes = list(self.getcodes())
            except ProcessException:
                pass

    def getscm(self):
        for name, scm in scms.items():
            if os.path.isdir(os.path.join(self.path, '.'+name)):
                return scm

    # Pass backend SCM commands and parameters if SCM exists
    def __wrap_scm(self, method):
        def __scm_call(*args, **kwargs):
            if self.scm and hasattr(self.scm, method) and callable(getattr(self.scm, method)):
                with cd(self.path):
                    return getattr(self.scm, method)(*args, **kwargs)
        return __scm_call

    def __getattr__(self, attr):
        if attr in ['geturl', 'getrev', 'add', 'remove', 'ignores', 'ignore', 'unignore',
                    'status', 'dirty', 'commit', 'outgoing', 'publish', 'checkout', 'update',
                    'isdetached']:
            wrapper = self.__wrap_scm(attr)
            self.__dict__[attr] = wrapper
            return wrapper
        else:
            raise AttributeError("Repo instance doesn't have attribute '%s'" % attr)

    def remove(self, dest, *args, **kwargs):
        if os.path.isfile(dest):
            try:
                os.remove(dest)
            except OSError:
                pass
        return self.scm.remove(dest, *args, **kwargs)

    def clone(self, url, path, rev=None, depth=None, protocol=None, **kwargs):
        # Sorted so repositories that match urls are attempted first
        sorted_scms = [(scm.isurl(url), scm) for scm in scms.values()]
        sorted_scms = filter(lambda (m, _): m, sorted_scms)

        for _, scm in sorted_scms:
            main = True
            cache = self.get_cache(url)

            # Try to clone with cache ref first
            if cache and not os.path.isdir(path):
                info("Found matching cached repository in \"%s\"" % cache)
                try:
                    if os.path.split(path)[0] and not os.path.isdir(os.path.split(path)[0]):
                        os.makedirs(os.path.split(path)[0])

                    info("Carbon copy from \"%s\" to \"%s\"" % (cache, path))
                    shutil.copytree(cache, path)

                    with cd(path):
                        scm.seturl(formaturl(url, protocol))
                        scm.cleanup()
                        info("Update cached copy from remote repository")
                        scm.update(rev, True)
                        main = False
                except (ProcessException, IOError):
                    info("Discarding cached repository")
                    if os.path.isdir(path):
                        rmtree_readonly(path)

            # Main clone routine if the clone with cache ref failed (might occur if cache ref is dirty)
            if main:
                try:
                    scm.clone(url, path, depth=depth, protocol=protocol, **kwargs)
                except ProcessException:
                    if os.path.isdir(path):
                        rmtree_readonly(path)
                    continue

            self.scm = scm
            self.url = url
            self.path = os.path.abspath(path)
            self.ignores()
            self.set_cache(url)
            return True

        return False

    def getlibs(self):
        for root, dirs, files in os.walk(self.path):
            dirs[:] = [d for d in dirs  if not d.startswith('.')]
            files[:] = [f for f in files if not f.startswith('.')]

            for f in files:
                if f.endswith('.component'):
                    repo = Repo.fromlib(os.path.join(root, f))
                    if repo:
                        yield repo
                    if f[:f.rfind('.')] in dirs:
                        dirs.remove(f[:f.rfind('.')])

    def getcodes(self):
        for root, dirs, files in os.walk(self.path):
            dirs[:] = [d for d in dirs  if not d.startswith('.')]
            files[:] = [f for f in files if not f.startswith('.')]

            for f in files:
                if f.endswith('.codes'):
                    repo = Repo.fromcode(os.path.join(root, f))
                    if repo:
                        yield repo
                    if f[:f.rfind('.')] in dirs:
                        dirs.remove(f[:f.rfind('.')])


    def write(self):
        if os.path.isfile(self.lib):
            with open(self.lib) as f:
                lib_repo = Repo.fromurl(f.read().strip())
                if (formaturl(lib_repo.url, 'https') == formaturl(self.url, 'https') # match URLs in common format (https)
                        and (lib_repo.rev == self.rev                              # match revs, even if rev is None (valid for repos with no revisions)
                             or (lib_repo.rev and self.rev
                                 and lib_repo.rev == self.rev[0:len(lib_repo.rev)]))):  # match long and short rev formats
                    #print self.name, 'unmodified'
                    return

        ref = (formaturl(self.url, 'https').rstrip('/') + '/' +
              (('' if self.is_build else '#') +
                self.rev if self.rev else ''))
        action("Updating reference \"%s\" -> \"%s\"" % (relpath(cwd_root, self.path) if cwd_root != self.path else self.name, ref))
        with open(self.lib, 'wb') as f:
            f.write(ref + '\n')

    def write_codes(self):
        if os.path.isfile(self.code):
            with open(self.code) as f:
                lib_repo = Repo.fromurl(f.read().strip())
                if (formaturl(lib_repo.url, 'ssh') == formaturl(self.url, 'ssh') # match URLs in common format (ssh)
                        and (lib_repo.rev == self.rev                              # match revs, even if rev is None (valid for repos with no revisions)
                             or (lib_repo.rev and self.rev
                                 and lib_repo.rev == self.rev[0:len(lib_repo.rev)]))):  # match long and short rev formats
                    #print self.name, 'unmodified'
                    return

        ref = (formaturl(self.url, 'ssh').rstrip('/') + '/' +
              (('' if self.is_build else '#') +
                self.rev if self.rev else ''))
        action("Updating reference \"%s\" -> \"%s\"" % (relpath(cwd_root, self.path) if cwd_root != self.path else self.name, ref))
        with open(self.code, 'wb') as f:
            f.write(ref + '\n')

    def rm_untracked(self):
        untracked = self.scm.untracked()
        for f in untracked:
            if re.match(r'(.+)\.(lib|bld)$', f) and os.path.isfile(f):
                action("Remove untracked library reference \"%s\"" % f)
                os.remove(f)

    def get_cache(self, url):
        up = urlparse(formaturl(url, 'https'))
        if self.cache and up and up.netloc and os.path.isdir(os.path.join(self.cache, up.netloc, re.sub(r'^/', '', up.path))):
            return os.path.join(self.cache, up.netloc, re.sub(r'^/', '', up.path))

    def set_cache(self, url):
        up = urlparse(formaturl(url, 'https'))
        if self.cache and up and up.netloc and os.path.isdir(self.path):
            try:
                cpath = os.path.join(self.cache, up.netloc, re.sub(r'^/', '', up.path))
                if not os.path.isdir(cpath):
                    os.makedirs(cpath)

                scm_dir = '.'+self.scm.name
                if os.path.isdir(os.path.join(cpath, scm_dir)):
                    rmtree_readonly(os.path.join(cpath, scm_dir))
                shutil.copytree(os.path.join(self.path, scm_dir), os.path.join(cpath, scm_dir))
            except Exception:
                warning("Unable to cache \"%s\" to \"%s\"" % (self.path, cpath))
        return False

    def can_update(self, clean, clean_deps):
        err = None
        if (self.is_local or self.url is None) and not clean_deps:
            err = (
                "Preserving local library \"%s\" in \"%s\".\nPlease publish this library to a remote URL to be able to restore it at any time."
                "You can use --ignore switch to ignore all local libraries and update only the published ones.\n"
                "You can also use --clean-deps switch to remove all local libraries. WARNING: This action cannot be undone." % (self.name, self.path))
        elif not clean and self.dirty():
            err = (
                "Uncommitted changes in \"%s\" in \"%s\".\nPlease discard or stash them first and then retry update.\n"
                "You can also use --clean switch to discard all uncommitted changes. WARNING: This action cannot be undone." % (self.name, self.path))
        elif not clean_deps and self.outgoing():
            err = (
                "Unpublished changes in \"%s\" in \"%s\".\nPlease publish them first using the \"publish\" command.\n"
                "You can also use --clean-deps to discard all local commits and replace the library with the one included in this revision. WARNING: This action cannot be undone." % (self.name, self.path))

        return (False, err) if err else (True, "OK")

    def check_repo(self, show_warning=None):
        err = None
        if not os.path.isdir(self.path):
            err = (
                "Library reference \"%s\" points to non-existing library in \"%s\"\n"
                "You can use \"yos deploy\" to import the missing libraries.\n"
                "You can also use \"yos sync\" to synchronize and remove all invalid library references." % (os.path.basename(self.lib), self.path))
        elif not self.isrepo(self.path):
            err = (
                "Library reference \"%s\" points to a folder \"%s\", which is not a valid repository.\n"
                "You can remove the conflicting folder manually and use \"yos deploy\" to import the missing libraries\n"
                "You can also remove library reference \"%s\" and use \"yos sync\" again." % (os.path.basename(self.lib), self.path, self.lib))

        if err:
            if show_warning:
                warning(err)
            else:
                error(err, 1)
            return False
        return True


# Program class, acts code base root
class Program(object):
    path = None
    name = None
    is_cwd = False
    is_repo = False
    is_classic = False
    build_dir = "BUILD"

    def __init__(self, path=None, print_warning=False):
        path = os.path.abspath(path or os.getcwd())
        self.path = path
        self.is_cwd = True

        while cd(path):
            tpath = path
            if os.path.isfile(os.path.join(path, Cfg.file)):
                self.path = path
                self.is_cwd = False
                break

            path = os.path.split(path)[0]
            if tpath == path:       # Reached root.
                break

        self.name = os.path.basename(self.path)
        self.is_classic = os.path.isfile(os.path.join(self.path, 'yos.bld'))

        # is_cwd flag indicates that current dir is assumed to be root, not root repo
        if self.is_cwd and print_warning:
            warning(
                "Could not find yos program in current path \"%s\".\n"
                "You can fix this by calling \"yos new .\" in the root of your program." % self.path)

    def get_cfg(self, *args, **kwargs):
        return Cfg(self.path).get(*args, **kwargs) or Global().get_cfg(*args, **kwargs)

    def set_cfg(self, *args, **kwargs):
        return Cfg(self.path).set(*args, **kwargs)

    def list_cfg(self, *args, **kwargs):
        return Cfg(self.path).list(*args, **kwargs)

    def set_root(self):
        return self.set_cfg('ROOT', '.')

    def unset_root(self, path=None):
        fl = os.path.join(path or self.path, Cfg.file)
        if os.path.isfile(fl):
            os.remove(fl)

    # Gets YOS dir (unified)
    def get_os_dir(self):
        if os.path.isdir(os.path.join(self.path, 'yos')):
            return os.path.join(self.path, 'yos')
        elif self.name == 'yos':
            return self.path
        else:
            return None

    def get_yoslib_dir(self):
        if os.path.isdir(os.path.join(self.path, 'yos')):
            return os.path.join(self.path, 'yos')
        else:
            return None

    # Gets yos tools dir (unified)
    def get_tools_dir(self):
        paths = []
        # yos dir identified and tools is a sub dir
        yos_os_path = self.get_os_dir()
        if yos_os_path:
            paths.append([yos_os_path, 'tools'])
            paths.append([yos_os_path, 'core', 'tools'])
        # yos not identified but tools found under cwd/tools
        paths.append([self.path, 'tools'])
        paths.append([self.path, 'core', 'tools'])
        # yos Classic deployed tools
        paths.append([self.path, '.temp', 'tools'])

        return self._find_file_paths(paths, 'make.py')

    def get_requirements(self):
        paths = []
        yos_os_path = self.get_os_dir()
        if yos_os_path:
            paths.append([yos_os_path, 'tools'])
            paths.append([yos_os_path])
        # yos not identified but tools found under cwd/tools
        paths.append([self.path, 'tools'])
        # yos Classic deployed tools
        paths.append([self.path, '.temp', 'tools'])
        # current dir
        paths.append([self.path])

        return self._find_file_paths(paths, 'requirements.txt')

    def _find_file_paths(self, paths, fl):
        for p in paths:
            path = os.path.join(*p)
            if os.path.isdir(path) and os.path.isfile(os.path.join(path, fl)):
                return os.path.join(path)
        return None

    def check_requirements(self, show_warning=False):
        req_path = self.get_requirements() or self.path
        req_file = 'requirements.txt'
        missing = []
        try:
            with open(os.path.join(req_path, req_file), 'r') as f:
                import pip
                installed_packages = [re.sub(r'-', '_', package.project_name.lower()) for package in pip.get_installed_distributions(local_only=True)]
                for line in f.read().splitlines():
                    pkg = re.sub(r'-', '_', re.sub(r'^([\w-]+).*$', r'\1', line).lower())
                    if not pkg in installed_packages:
                        missing.append(pkg)

                if missing and install_requirements:
                    try:
                        action("Auto-installing missing Python modules...")
                        pquery(['pip', 'install', '-q', '-r', os.path.join(req_path, req_file)])
                        missing = []
                    except ProcessException:
                        warning("Unable to auto-install required Python modules.")

        except (IOError, ImportError, OSError):
            pass

        if missing:
            err = (
                "-----------------------------------------------------------------\n"
                "The yos OS tools in this program require the following Python modules: %s\n"
                "You can install all missing modules by running \"pip install -r %s\" in \"%s\"" % (', '.join(missing), req_file, req_path))
            if os.name == 'posix':
                err += "\nOn Posix systems (Linux, Mac, etc) you might have to switch to superuser account or use \"sudo\""

            if show_warning:
                warning(err)
            else:
                error(err, 1)


    # Routines after cloning yos
    def post_action(self):
        yos_tools_path = self.get_tools_dir()

        if not yos_tools_path and (self.is_classic or os.path.exists(os.path.join(self.path, Cfg.file))):
            self.add_tools(os.path.join(self.path, '.temp'))
            yos_tools_path = self.get_tools_dir()

        if not yos_tools_path:
            warning("Cannot find the yos tools directory in \"%s\"" % self.path)
            return False

        if (not os.path.isfile(os.path.join(self.path, 'yos_settings.py')) and
                os.path.isfile(os.path.join(yos_tools_path, 'default_settings.py'))):
            shutil.copy(os.path.join(yos_tools_path, 'default_settings.py'), os.path.join(self.path, 'yos_settings.py'))

        self.check_requirements(True)

    def add_tools(self, path):
        if not os.path.exists(path):
            os.mkdir(path)
        with cd(path):
            tools_dir = 'tools'
            if not os.path.exists(tools_dir):
                try:
                    action("Couldn't find build tools in your program. Downloading the yos 2.0 SDK tools...")
                    repo = Repo.fromurl(yos_sdk_tools_url)
                    repo.clone(yos_sdk_tools_url, tools_dir)
                except Exception:
                    if os.path.exists(tools_dir):
                        rmtree_readonly(tools_dir)
                    error("An error occurred while cloning the yos SDK tools from \"%s\"" % yos_sdk_tools_url)

    def update_tools(self, path):
        tools_dir = 'tools'
        if os.path.exists(os.path.join(path, tools_dir)):
            with cd(os.path.join(path, tools_dir)):
                try:
                    action("Updating the yos 2.0 SDK tools...")
                    repo = Repo.fromrepo()
                    repo.update()
                except Exception:
                    error("An error occurred while update the yos SDK tools from \"%s\"" % yos_sdk_tools_url)

    def get_tools(self):
        yos_tools_path = self.get_tools_dir()
        if not yos_tools_path:
            error('The yos tools were not found in "%s". \nRun `yos deploy` to install dependencies and tools. ' % self.path, -1)
        return yos_tools_path

    def get_env(self):
        env = os.environ.copy()
        env['PYTHONPATH'] = os.path.abspath(self.path)
        compilers = ['ARM', 'GCC_ARM', 'IAR']
        for c in compilers:
            if self.get_cfg(c+'_PATH'):
                env['YOS_'+c+'_PATH'] = self.get_cfg(c+'_PATH')

        return env

    def get_target(self, target=None):
        target_cfg = self.get_cfg('TARGET')
        target = target if target else target_cfg

        if target and (target.lower() == 'detect' or target.lower() == 'auto'):
            targets = self.get_detected_targets()
            if targets == False:
                error("The target detection requires that the 'yos-ls' python module is installed.\nYou can install yos-ls by running 'pip install yos-ls'.")
            elif len(targets) > 1:
                error("Multiple targets were detected.\nOnly 1 target board should be connected to your system when you use the '-m auto' switch.")
            elif len(targets) == 0:
                error("No targets were detected.\nPlease make sure a target board is connected to this system.")
            else:
                action("Detected \"%s\" connected to \"%s\" and using com port \"%s\"" % (targets[0]['name'], targets[0]['mount'], targets[0]['serial']))
                target = targets[0]['name']

        if target is None:
            error("Please specify target using the -m switch or set default target using command 'yos target'", 1)
        return target

    def get_toolchain(self, toolchain=None):
        toolchain_cfg = self.get_cfg('TOOLCHAIN')
        tchain = toolchain if toolchain else toolchain_cfg
        if tchain is None:
            error("Please specify toolchain using the -t switch or set default toolchain using command 'yos toolchain'", 1)
        return tchain

    def set_defaults(self, target=None, toolchain=None):
        if target and not self.get_cfg('TARGET'):
            self.set_cfg('TARGET', target)
        if toolchain and not self.get_cfg('TOOLCHAIN'):
            self.set_cfg('TOOLCHAIN', toolchain)

    def get_macros(self):
        macros = []
        if os.path.isfile('MACROS.txt'):
            with open('MACROS.txt') as f:
                macros = f.read().splitlines()
        return macros


    def ignore_build_dir(self):
        build_path = os.path.join(self.path, self.build_dir)
        if not os.path.exists(build_path):
            os.mkdir(build_path)
        if not os.path.exists(os.path.join(build_path, '.yosignore')):
            try:
                with open(os.path.join(build_path, '.yosignore'), 'w') as f:
                    f.write('*\n')
            except IOError:
                error("Unable to write build ignore file in \"%s\"" % os.path.join(build_path, '.yosignore'), 1)

    def get_detected_targets(self):
        targets = []
        try:
            import yos_lstools
            oldError = None
            if os.name == 'nt':
                oldError = ctypes.windll.kernel32.SetErrorMode(1) # Disable Windows error box temporarily. note that SEM_FAILCRITICALERRORS = 1
            yoss = yos_lstools.create()
            detect_muts_list = yoss.list_yoss()
            if os.name == 'nt':
                ctypes.windll.kernel32.SetErrorMode(oldError)

            for mut in detect_muts_list:
                targets.append({
                    'id': mut['target_id'], 'name': mut['platform_name'],
                    'mount': mut['mount_point'], 'serial': mut['serial_port']
                })
        except (IOError, ImportError, OSError):
            return False

        return targets


# Global class used for global config
class Global(object):
    def __init__(self):
        self.path = os.path.join(os.path.expanduser("~"), '.yos')
        if not os.path.exists(self.path):
            try:
                os.mkdir(self.path)
            except (IOError, OSError):
                pass

    def get_cfg(self, *args, **kwargs):
        return Cfg(self.path).get(*args, **kwargs)

    def set_cfg(self, *args, **kwargs):
        return Cfg(self.path).set(*args, **kwargs)

    def list_cfg(self, *args, **kwargs):
        return Cfg(self.path).list(*args, **kwargs)

# Cfg classed used for handling the config backend
class Cfg(object):
    path = None
    file = ".yos"

    def __init__(self, path):
        self.path = path

    # Sets config value
    def set(self, var, val):
        if not re.match(r'^([\w+-]+)$', var):
            error("%s is invalid config variable name" % var)

        fl = os.path.join(self.path, self.file)
        try:
            with open(fl) as f:
                lines = f.read().splitlines()
        except (IOError, OSError):
            lines = []

        for line in lines:
            m = re.match(r'^([\w+-]+)\=(.*)$', line)
            if m and m.group(1) == var:
                lines.remove(line)

        if not val is None:
            lines += [var+"="+val]

        try:
            with open(fl, 'w') as f:
                f.write('\n'.join(lines) + '\n')
        except (IOError, OSError):
            warning("Unable to write config file %s" % fl)

    # Gets config value
    def get(self, var, default_val=None):
        fl = os.path.join(self.path, self.file)
        try:
            with open(fl) as f:
                lines = f.read().splitlines()
        except (IOError, OSError):
            lines = []

        for line in lines:
            m = re.match(r'^([\w+-]+)\=(.*)$', line)
            if m and m.group(1) == var:
                return m.group(2)
        return default_val

    # Get all config var/values pairs
    def list(self):
        fl = os.path.join(self.path, self.file)
        try:
            with open(fl) as f:
                lines = f.read().splitlines()
        except (IOError, OSError):
            lines = []

        vars = {}
        for line in lines:
            m = re.match(r'^([\w+-]+)\=(.*)$', line)
            if m and m.group(1) and m.group(1) != 'ROOT':
                vars[m.group(1)] = m.group(2)
        return vars


def formaturl(url, format="default"):
    url = "%s" % url
    m = re.match(regex_yos_url, url)
    if m:
        if format == "http":
            url = 'http://%s/%s/%s/%s/%s' % (m.group(2), m.group(4), m.group(5), m.group(6), m.group(7))
        else:
            url = 'https://%s/%s/%s/%s/%s' % (m.group(2), m.group(4), m.group(5), m.group(6), m.group(7))
    else:
        m = re.match(regex_git_url, url)
        if m:
            if format == "ssh":
                url = 'ssh://%s%s/%s.git' % (m.group(2) or 'git@', m.group(6), m.group(7))
            elif format == "http":
                url = 'http://%s%s/%s' % (m.group(2) if (m.group(2) and (m.group(5) or m.group(3) != 'git')) else '', m.group(6), m.group(7))
            elif format == "https":
                url = 'https://%s%s/%s%s' % (m.group(2) if (m.group(2) and (m.group(5) or m.group(3) != 'git')) else '', m.group(6), m.group(7), m.group(8))
        else:
            m = re.match(regex_hg_url, url)
            if m:
                if format == "ssh":
                    url = 'ssh://%s/%s' % (m.group(2), m.group(3))
                elif format == "http":
                    url = 'http://%s/%s' % (m.group(2), m.group(3))
                elif format == "https":
                    url = 'https://%s/%s' % (m.group(2), m.group(3))
    return url

def get_yosder_dir():
    # Find the yos_toolchain directory
    builtin_yosder = os.path.join(Program().path,'yos/yos_toolchain')
    yosder_dir = Program().get_cfg('yos_toolchain') or Global().get_cfg('yos_toolchain') or \
    (builtin_yosder if os.path.isdir(builtin_yosder) else None)
    if not yosder_dir:
        error('Can not find yos_toolchain!')
    return yosder_dir

def _run_make(arg_list):
    # yosder_dir = get_yosder_dir()
    yosder_dir = 'build'

    # Decide which make to use according to the platform system 
    win_make = os.path.join(yosder_dir,'cmd/Win32/make.exe')
    mac_make = os.path.join(yosder_dir,'cmd/OSX/make')
    linux_make = os.path.join(yosder_dir,'cmd/Linux64/make')
    make_cmd = mac_make if sys.platform == 'darwin' else (linux_make if sys.platform == 'linux2' else (win_make if sys.platform == 'win32' else None))
    if not make_cmd:
        error('Unsupported system!')

    # Run make command
    host_os = 'OSX' if sys.platform == 'darwin' else 'Linux64' if sys.platform == 'linux2' else 'Win32'
    make_cmd_str = ' '.join([make_cmd, 'HOST_OS='+host_os, 'TOOLS_ROOT='+yosder_dir] + list(arg_list))
    os.system(make_cmd_str)

# Subparser handling
parser = argparse.ArgumentParser(prog='yos',
    description="Code management tool for YOS - https://code.aliyun.com/yos/yos\nversion %s\n\nUse 'yos <command> -h|--help' for detailed help.\nOnline manual and guide available at https://code.aliyun.com/yos/yos-cube" % ver,
    formatter_class=argparse.RawTextHelpFormatter)
subparsers = parser.add_subparsers(title="Commands", metavar="           ")
parser.add_argument("--version", action="store_true", dest="version", help="print version number and exit")
subcommands = {}

# Process handling
def subcommand(name, *args, **kwargs):
    def __subcommand(command):
        if not kwargs.get('description') and kwargs.get('help'):
            kwargs['description'] = kwargs['help']
        if not kwargs.get('formatter_class'):
            kwargs['formatter_class'] = argparse.RawDescriptionHelpFormatter

        subparser = subparsers.add_parser(name, **kwargs)
        subcommands[name] = subparser

        for arg in args:
            arg = dict(arg)
            opt = arg['name']
            del arg['name']

            if isinstance(opt, basestring):
                subparser.add_argument(opt, **arg)
            else:
                subparser.add_argument(*opt, **arg)

        subparser.add_argument("-v", "--verbose", action="store_true", dest="verbose", help="Verbose diagnostic output")
        subparser.add_argument("-vv", "--very_verbose", action="store_true", dest="very_verbose", help="Very verbose diagnostic output")

        def thunk(parsed_args):
            argv = [arg['dest'] if 'dest' in arg else arg['name'] for arg in args]
            argv = [(arg if isinstance(arg, basestring) else arg[-1]).strip('-').replace('-', '_')
                    for arg in argv]
            argv = {arg: vars(parsed_args)[arg] for arg in argv
                    if vars(parsed_args)[arg] is not None}

            return command(**argv)

        subparser.set_defaults(command=thunk)
        return command
    return __subcommand


# New command
@subcommand('new',
    dict(name='name', help='Destination name or path'),
    dict(name='--scm', nargs='?', help='Source control management. Currently supported: %s. Default: git' % ', '.join([s.name for s in scms.values()])),
    dict(name='--program', action='store_true', help='Force creation of an yos program. Default: auto.'),
    dict(name='--component', action='store_true', help='Force creation of an yos component. Default: auto.'),
    dict(name='--yoslib', action='store_true', help='Add the yos component instead of yos into the program.'),
    dict(name='--create-only', action='store_true', help='Only create a program, do not import yos or yos component.'),
    dict(name='--depth', nargs='?', help='Number of revisions to fetch the yos OS repository when creating new program. Default: all revisions.'),
    dict(name='--protocol', nargs='?', help='Transport protocol when fetching the yos OS repository when creating new program. Supported: https, http, ssh, git. Default: inferred from URL.'),
    help='Create new yos program or component',
    description=(
        "Creates a new yos program if executed within a non-program location.\n"
        "Alternatively creates an yos component if executed within an existing program.\n"
        "When creating new program, the latest yos release will be downloaded/added\n unless --create-only is specified.\n"
        "Supported source control management: git, hg"))
def new(name, scm='git', program=False, component=False, yoslib=False, create_only=False, depth=None, protocol=None):
    global cwd_root

    d_path = os.path.abspath(name or os.getcwd())
    p_path = os.path.dirname(d_path)
    if program and component:
        error("Cannot use both --program and --component options.", 1)
    elif program or component:
        d_type = 'component' if component else 'program'
    else:
        pp = Program(p_path)
        pd = Program(d_path)
        if pp.path == pd.path:
            d_type = 'component' if os.path.abspath(p_path) != os.path.abspath(d_path) else 'program'
        else:
            d_type = 'component' if not pp.is_cwd and os.path.abspath(p_path) != os.path.abspath(d_path) else 'program'

    if os.path.exists(d_path):
        p = Program(d_path)
        if (d_type == 'program' and not p.is_cwd) or (d_type == 'component' and Repo.isrepo(d_path)):
            error("A %s with name \"%s\" already exists." % (d_type, os.path.basename(d_path)), 1)

    if scm and scm != 'none':
        if os.path.isdir(d_path) and Repo.isrepo(d_path):
            repo = Repo.fromrepo(d_path)
            if repo.scm.name != scm:
                error("A repository already exists in \"%s\" based on %s. Please select a different name or location." % (d_path, scm), 1)
        else:
            repo_scm = [s for s in scms.values() if s.name == scm.lower()]
            if not repo_scm:
                error(
                    "You have specified invalid source control management system\n"
                    "Please specify one of the following SCMs: %s" % ', '.join([s.name for s in scms.values()]), 1)
            repo_scm[0].init(d_path)
    else:
        scm = 'folder'
        if not os.path.isdir(d_path):
            os.mkdir(d_path)

    if len(os.listdir(d_path)) > 1:
        warning("Directory \"%s\" is not empty." % d_path)

    action("Creating new %s \"%s\" (%s)" % (d_type, os.path.basename(d_path), scm))
    p = Program(d_path)
    if d_type == 'program':
        # This helps sub-commands to display relative paths to the created program
        cwd_root = os.path.abspath(d_path)
        p.path = cwd_root
        p.set_root()
        if not create_only and not p.get_os_dir() and not p.get_yoslib_dir():
            url = yos_lib_url if yoslib else yos_os_url+'#latest'
            d = 'yos' if yoslib else 'yos'
            try:
                with cd(d_path):
                    add(url, depth=depth, protocol=protocol, top=False)
            except Exception as e:
                if os.path.isdir(os.path.join(d_path, d)):
                    rmtree_readonly(os.path.join(d_path, d))
                raise e
        if d_path:
            os.chdir(d_path)
            Repo.fromrepo().ignores()
    else:
        p.unset_root(d_path)
        with cd(p_path):
            sync()

    # Copy template files
    if d_type == 'program':
        target_dir = d_path
        target_name = Program().name
        target_file_list = ('template/main.c', 'template/yos_config.h', 'README.md', 'template/template.mk')
        temp_dir = os.path.join(d_path, 'yos/template/program')
        os.mkdir(os.path.join(d_path, target_name))
    else:
        target_dir = d_path
        target_name = name
        target_file_list = ('template.c', 'template.h', 'README.md', 'template.mk', 'test/README.md', 'test/main.c', 'test/yos_config.h', 'test/test.mk')
        temp_dir = os.path.join(p_path, 'yos/template/component')
        os.mkdir(os.path.join(d_path, 'test'))
        os.chdir(d_path)

    for file in target_file_list:
        with open(os.path.join(temp_dir, file), 'r') as f:
            content = f.read()
        target_file_name = file.replace('template', target_name)
        target_file_content = content.replace('template', target_name)
        target_file_path = os.path.join(target_dir, target_file_name)
        with open(target_file_path, 'w') as f:
            f.write(target_file_content)
        Repo.fromrepo().add(target_file_path)
    
#    Program(d_path).post_action()


# Import command
@subcommand('import',
    dict(name='url', help='URL of the program'),
    dict(name='path', nargs='?', help='Destination name or path. Default: current directory.'),
    dict(name=['-I', '--ignore'], action='store_true', help='Ignore errors related to cloning and updating.'),
    dict(name='--depth', nargs='?', help='Number of revisions to fetch from the remote repository. Default: all revisions.'),
    dict(name='--protocol', nargs='?', help='Transport protocol for the source control management. Supported: https, http, ssh, git. Default: inferred from URL.'),
    help='Import program from URL',
    description=(
        "Imports yos program and its dependencies from a source control based URL\n"
        "(GitHub, Bitbucket, yos.org) into the current directory or specified\npath.\n"
        "Use 'yos add <URL>' to add a component into an existing program."))
def import_(url, path=None, ignore=False, depth=None, protocol=None, top=True):
    global cwd_root

    # translate 'yos' to https://code.aliyun.com/yos
    if not Repo.isurl(url) and not os.path.exists(url):
        url = yos_base_url+'/'+url+'.git'

    repo = Repo.fromurl(url, path)
    if top:
        p = Program(path)
        if p and not p.is_cwd:
            error("Cannot import program in the specified location \"%s\" because it's already part of a program \"%s\".\n"
                  "Please change your working directory to a different location or use \"yos add\" to import the URL as a component." % (os.path.abspath(repo.path), p.name), 1)

    protocol = Program().get_cfg('PROTOCOL', protocol)

    if os.path.isdir(repo.path) and len(os.listdir(repo.path)) > 1:
        error("Directory \"%s\" is not empty. Please ensure that the destination folder is empty." % repo.path, 1)

    text = "Importing program" if top else "Adding component"
    action("%s \"%s\" from \"%s\"%s" % (text, relpath(cwd_root, repo.path), formaturl(repo.url, protocol), ' at '+(repo.revtype(repo.rev, True))))
    if repo.clone(repo.url, repo.path, rev=repo.rev, depth=depth, protocol=protocol):
        with cd(repo.path):
            Program(repo.path).set_root()
            try:
                if repo.rev and repo.getrev() != repo.rev:
                    repo.checkout(repo.rev, True)
            except ProcessException as e:
                err = "Unable to update \"%s\" to %s" % (repo.name, repo.revtype(repo.rev, True))
                if depth:
                    err = err + ("\nThe --depth option might prevent fetching the whole revision tree and checking out %s." % (repo.revtype(repo.rev, True)))
                if ignore:
                    warning(err)
                else:
                    error(err, e[0])
    else:
        err = "Unable to clone repository (%s)" % url
        if ignore:
            warning(err)
        else:
            error(err, 1)
                
    if os.path.isdir(repo.path):
        repo.sync()

        if top: # This helps sub-commands to display relative paths to the imported program
            cwd_root = repo.path

        if repo.name == 'yos':
            target_dir = Program().path
            target_name = Program().name
            target_file_list = ('.project', '.cproject')
            eclipse_subdir = 'Win32' if sys.platform == 'win32' else ('OSX' if sys.platform == 'darwin' else 'Linux64')
            temp_dir = os.path.join(Program().path, 'yos/makefiles/eclipse_project', eclipse_subdir)
            for file in target_file_list:
                with open(os.path.join(temp_dir, file), 'r') as f:
                    content = f.read()
                target_file_name = file
                target_file_content = content.replace('template', target_name)
                target_file_path = os.path.join(target_dir, target_file_name)
                with open(target_file_path, 'w') as f:
                    f.write(target_file_content)

        with cd(repo.path):
            deploy(ignore=ignore, depth=depth, protocol=protocol, top=False)

#    if top:
#        Program(repo.path).post_action()


# Add component command
@subcommand('add',
    dict(name='url', help='URL of the component'),
    dict(name='path', nargs='?', help='Destination name or path. Default: current folder.'),
    dict(name=['-I', '--ignore'], action='store_true', help='Ignore errors related to cloning and updating.'),
    dict(name='--depth', nargs='?', help='Number of revisions to fetch from the remote repository. Default: all revisions.'),
    dict(name='--protocol', nargs='?', help='Transport protocol for the source control management. Supported: https, http, ssh, git. Default: inferred from URL.'),
    help='Add component from URL',
    description=(
        "Adds yos component and its dependencies from a source control based URL\n"
        "(GitHub, Bitbucket, yos.org) into an existing program.\n"
        "Use 'yos import <URL>' to import as a program"))
def add(url, path=None, ignore=False, depth=None, protocol=None, top=True):
     # translate 'yos' to https://code.aliyun.com/yos
    if not Repo.isurl(url) and not os.path.exists(url):
        url = yos_base_url+'/'+url+'.git'
        
    repo = Repo.fromrepo()

    lib = Repo.fromurl(url, path)
    import_(lib.fullurl, lib.path, ignore=ignore, depth=depth, protocol=protocol, top=False)
    repo.ignore(relpath(repo.path, lib.path))
    lib.sync()

    lib.write()
    repo.add(lib.lib)

#    if top:
#        Program(repo.path).post_action()


# Remove component
@subcommand('remove',
    dict(name='path', help='Local component name or path'),
    help='Remove component',
    description=(
        "Remove specified component, its dependencies and references from the current\n"
        "You can re-add the component from it's URL via 'yos add <component URL>'."))
def remove(path):
    repo = Repo.fromrepo()
    if not Repo.isrepo(path):
        error("Could not find component in path (%s)" % path, 1)

    lib = Repo.fromrepo(path)
    action("Removing component \"%s\" in \"%s\"" % (lib.name, lib.path))
    rmtree_readonly(lib.path)
    repo.remove(lib.lib)
    repo.unignore(relpath(repo.path, lib.path))


# Deploy command
@subcommand('deploy',
    dict(name=['-I', '--ignore'], action='store_true', help='Ignore errors related to cloning and updating.'),
    dict(name='--depth', nargs='?', help='Number of revisions to fetch from the remote repository. Default: all revisions.'),
    dict(name='--protocol', nargs='?', help='Transport protocol for the source control management. Supported: https, http, ssh, git. Default: inferred from URL.'),
    help='Find and add missing components and source codes',
    description=(
        "Import missing dependencies in an existing program or component.\n"
        "Use 'yos import <URL>' and 'yos add <URL>' instead of cloning manually and\n"
        "then running 'yos deploy'"))
def deploy(ignore=False, depth=None, protocol=None, top=True):
    repo = Repo.fromrepo()
    repo.ignores()

    for lib in repo.libs:
        if os.path.isdir(lib.path):
            if lib.check_repo():
                with cd(lib.path):
                    update(lib.rev, ignore=ignore, depth=depth, protocol=protocol, top=False)
        else:
            import_(lib.fullurl, lib.path, ignore=ignore, depth=depth, protocol=protocol, top=False)
            repo.ignore(relpath(repo.path, lib.path))

#    if top:
#        program = Program(repo.path)
#        program.post_action()
#        if program.is_classic:
#            program.update_tools('.temp')

# Source command
@subcommand('codes',
    dict(name='name', help='Destination component name without suffix'),
    dict(name=['-I', '--ignore'], action='store_true', help='Ignore errors related to cloning and updating.'),
    dict(name='--depth', nargs='?', help='Number of revisions to fetch from the remote repository. Default: all revisions.'),
    dict(name='--protocol', nargs='?', help='Transport protocol for the source control management. Supported: https, http, ssh, git. Default: inferred from URL.'),
    help='Import the optional component from the remote repository',
    description=(
        "Import optional component defined by .codes file.\n"
        "name of the .codes file should be specified ."))
def codes(name, ignore=False, depth=None, protocol=None, top=True):
    repo = Repo.fromrepo()
    code = Repo.fromcode(os.path.join(os.getcwd(), name+'.codes'))

    if os.path.isdir(code.path):
        if code.check_repo():
            with cd(code.path):
                update(code.rev, ignore=ignore, depth=depth, protocol=protocol, top=False)
    else:
        import_(code.fullurl, code.path, ignore=ignore, depth=depth, protocol=protocol, top=False)
        print '>>>>',repo.path,code.path
        repo.ignore(relpath(repo.path, code.path))
            

# Publish command
@subcommand('publish',
    dict(name=['-A', '--all'], dest='all_refs', action='store_true', help='Publish all branches, including new ones. Default: push only the current branch.'),
    dict(name=['-M', '--message'], dest='msg', type=str, nargs='?', help='Commit message. Default: prompts for commit message.'),
    help='Publish program or component',
    description=(
        "Publishes the current program or component and all dependencies to their\nassociated remote repository URLs.\n"
        "This command performs various consistency checks for local uncommitted changes\n"
        "and unpublished revisions and encourages to commit/push them.\n"
        "Online guide about collaboration is available at:\n"
        "www.yos.com/collab_guide"))
def publish(all_refs=None, msg=None, top=True):
    if top:
        action("Checking for local modifications...")

    repo = Repo.fromrepo()
    if repo.is_local:
        error(
            "%s \"%s\" in \"%s\" with %s is a local repository.\nPlease associate it with a remote repository URL before attempting to publish.\n"
            "Read more about publishing local repositories here:\nhttps://code.aliyun.com/yos/yos-cube/#publishing-local-program-or-component" % ("Program" if top else "Library", repo.name, repo.path, repo.scm.name), 1)

    for lib in repo.libs:
        if lib.check_repo():
            with cd(lib.path):
                progress()
                publish(all_refs, msg=msg, top=False)

    sync(recursive=False)

    if repo.dirty():
        action("Uncommitted changes in %s \"%s\" in \"%s\"" % (repo.pathtype(repo.path), repo.name, repo.path))
        if msg:
            repo.commit(msg)
        else:
            raw_input('Press enter to commit and publish: ')
            repo.commit()

    try:
        outgoing = repo.outgoing()
        if outgoing > 0:
            action("Pushing local repository \"%s\" to remote \"%s\"" % (repo.name, repo.url))
            repo.publish(all_refs)
        else:
            if top:
                action("Nothing to publish to the remote repository (the source tree is unmodified)")
    except ProcessException as e:
        if e[0] != 1:
            raise e


# Update command
@subcommand('update',
    dict(name='rev', nargs='?', help='Revision, tag or branch'),
    dict(name=['-C', '--clean'], action='store_true', help='Perform a clean update and discard all modified or untracked files. WARNING: This action cannot be undone. Use with caution.'),
    dict(name='--clean-files', action='store_true', help='Remove any local ignored files. Requires \'--clean\'. WARNING: This will wipe all local uncommitted, untracked and ignored files. Use with extreme caution.'),
    dict(name='--clean-deps', action='store_true', help='Remove any local libraries and also libraries containing uncommitted or unpublished changes. Requires \'--clean\'. WARNING: This action cannot be undone. Use with caution.'),
    dict(name=['-I', '--ignore'], action='store_true', help='Ignore errors related to unpublished libraries, unpublished or uncommitted changes, and attempt to update from associated remote repository URLs.'),
    dict(name='--depth', nargs='?', help='Number of revisions to fetch from the remote repository. Default: all revisions.'),
    dict(name='--protocol', nargs='?', help='Transport protocol for the source control management. Supported: https, http, ssh, git. Default: inferred from URL.'),
    help='Update to branch, tag, revision or latest',
    description=(
        "Updates the current program or component and its dependencies to specified\nbranch, tag or revision.\n"
        "Alternatively fetches from associated remote repository URL and updates to the\n"
        "latest revision in the current branch."))
def update(rev=None, clean=False, clean_files=False, clean_deps=False, ignore=False, top=True, depth=None, protocol=None):
    if top and clean:
        sync()

    cwd_type = Repo.pathtype(cwd_root)
    cwd_dest = "program" if cwd_type == "directory" else "component"

    repo = Repo.fromrepo()
    # A copy of repo containing the .lib layout before updating
    repo_orig = Repo.fromrepo()

    if top and not rev and repo.isdetached():
        error(
            "This %s is in detached HEAD state, and you won't be able to receive updates from the remote repository until you either checkout a branch or create a new one.\n"
            "You can checkout a branch using \"%s checkout <branch_name>\" command before running \"yos update\"." % (cwd_type, repo.scm.name), 1)

    if repo.is_local and not repo.rev:
        action("Skipping unpublished empty %s \"%s\"" % (
            cwd_type if top else cwd_dest,
            os.path.basename(repo.path) if top else relpath(cwd_root, repo.path)))
    else:
        # Fetch from remote repo
        action("Updating %s \"%s\" to %s" % (
            cwd_type if top else cwd_dest,
            os.path.basename(repo.path) if top else relpath(cwd_root, repo.path),
            repo.revtype(rev, True)))

        try:
            repo.update(rev, clean, clean_files, repo.is_local)
        except ProcessException as e:
            err = "Unable to update \"%s\" to %s" % (repo.name, repo.revtype(rev, True))
            if depth:
                err = err + ("\nThe --depth option might prevent fetching the whole revision tree and checking out %s." % (repo.revtype(repo.rev, True)))
            if ignore:
                warning(err)
            else:
                error(err, e[0])

        repo.rm_untracked()
        if top and cwd_type == 'component':
            repo.sync()
            repo.write()

    # Compare component references (.lib) before and after update, and remove libraries that do not have references in the current revision
    for lib in repo_orig.libs:
        if not os.path.isfile(lib.lib) and os.path.isdir(lib.path): # Library reference doesn't exist in the new revision. Will try to remove component to reproduce original structure
            gc = False
            with cd(lib.path):
                lib_repo = Repo.fromrepo(lib.path)
                gc, msg = lib_repo.can_update(clean, clean_deps)
            if gc:
                action("Removing component \"%s\" (obsolete)" % (relpath(cwd_root, lib.path)))
                rmtree_readonly(lib.path)
                repo.unignore(relpath(repo.path, lib.path))
            else:
                if ignore:
                    warning(msg)
                else:
                    error(msg, 1)

    # Reinitialize repo.libs() to reflect the component files after update
    repo.sync()

    # Recheck libraries as their urls might have changed
    for lib in repo.libs:
        if os.path.isdir(lib.path) and Repo.isrepo(lib.path):
            lib_repo = Repo.fromrepo(lib.path)
            if (not lib.is_local and not lib_repo.is_local and
                formaturl(lib.url, 'https') != formaturl(lib_repo.url, 'https')): # Repository URL has changed
                gc = False
                with cd(lib.path):
                    gc, msg = lib_repo.can_update(clean, clean_deps)
                if gc:
                    action("Removing component \"%s\" (changed URL). Will add from new URL." % (relpath(cwd_root, lib.path)))
                    rmtree_readonly(lib.path)
                    repo.unignore(relpath(repo.path, lib.path))
                else:
                    if ignore:
                        warning(msg)
                    else:
                        error(msg, 1)

    # Import missing repos and update to revs
    for lib in repo.libs:
        if not os.path.isdir(lib.path):
            import_(lib.fullurl, lib.path, ignore=ignore, depth=depth, protocol=protocol, top=False)
            repo.ignore(relpath(repo.path, lib.path))
        else:
            with cd(lib.path):
                update(lib.rev, clean=clean, clean_files=clean_files, clean_deps=clean_deps, ignore=ignore, top=False)

#    if top:
#        program = Program(repo.path)
#        program.set_root()
#        program.post_action()
#        if program.is_classic:
#            program.update_tools('.temp')


# Synch command
@subcommand('sync',
    help='Synchronize yos component references',
    description=(
        "Synchronizes all component and dependency references (.component files) in the\n"
        "current program or component.\n"
        "Note that this will remove all invalid component references."))
def sync(recursive=True, keep_refs=False, top=True):
    if top and recursive:
        action("Synchronizing dependency references...")

    repo = Repo.fromrepo()
    repo.ignores()

    for lib in repo.libs:
        if os.path.isdir(lib.path):
            lib.check_repo()
            lib.sync()
            lib.write()
            repo.ignore(relpath(repo.path, lib.path))
            progress()
        else:
            if not keep_refs:
                action("Removing reference \"%s\" -> \"%s\"" % (lib.name, lib.fullurl))
                repo.remove(lib.lib)
                repo.unignore(relpath(repo.path, lib.path))

    for code in repo.codes:
        if os.path.isdir(code.path):
            code.check_repo()
            code.sync()
            code.write_codes()
            repo.ignore(relpath(repo.path, code.path))
            progress()

    for root, dirs, files in os.walk(repo.path):
        dirs[:] = [d for d in dirs  if not d.startswith('.')]
        files[:] = [f for f in files if not f.startswith('.')]

        for d in list(dirs):
            if not Repo.isrepo(os.path.join(root, d)):
                continue

            lib = Repo.fromrepo(os.path.join(root, d))
            if os.path.isfile(lib.lib) or os.path.isfile(lib.code):
                dirs.remove(d)
                continue

            dirs.remove(d)
            lib.write()
            repo.ignore(relpath(repo.path, lib.path))
            repo.add(lib.lib)
            progress()

    repo.sync()

    if recursive:
        for lib in repo.libs:
            if lib.check_repo():
                with cd(lib.path):
                    sync(keep_refs=keep_refs, top=False)

    # Update the .lib reference in the parent repository
    cwd_type = Repo.pathtype(cwd_root)
    if top and cwd_type == "component":
        repo = Repo.fromrepo()
        repo.write()


# List command
@subcommand('ls',
    dict(name=['-a', '--all'], dest='detailed', action='store_true', help='List repository URL and revision pairs'),
    dict(name=['-I', '--ignore'], action='store_true', help='Ignore errors related to missing libraries.'),
    help='View dependency tree',
    description=(
        "View the dependency tree of the current program or component."))
def list_(detailed=False, prefix='', p_path=None, ignore=False):
    repo = Repo.fromrepo()

    print "%s (%s)" % (prefix + (relpath(p_path, repo.path) if p_path else repo.name), ((repo.url+('#'+str(repo.rev)[:12] if repo.rev else '') if detailed else str(repo.rev)[:12]) or 'no revision'))

    for i, lib in enumerate(sorted(repo.libs, key=lambda l: l.path)):
        if prefix:
            nprefix = prefix[:-3] + ('|  ' if prefix[-3] == '|' else '   ')
        else:
            nprefix = ''
        nprefix += '|- ' if i < len(repo.libs)-1 else '`- '

        if lib.check_repo(ignore):
            with cd(lib.path):
                list_(detailed, nprefix, repo.path, ignore=ignore)


# Command status for cross-SCM status of repositories
@subcommand('status',
    dict(name=['-I', '--ignore'], action='store_true', help='Ignore errors related to missing libraries.'),
    help='Show version control status\n\n',
    description=(
        "Show uncommitted changes a program or component and its dependencies."))
def status_(ignore=False):
    repo = Repo.fromrepo()
    if repo.dirty():
        action("Status for \"%s\":" % repo.name)
        log(repo.status()+"\n")

    for lib in repo.libs:
        if lib.check_repo(ignore):
            with cd(lib.path):
                status_(ignore)

'''
# Compile command which invokes the yos OS native build system
@subcommand('compile',
    dict(name=['-t', '--toolchain'], help='Compile toolchain. Example: ARM, GCC_ARM, IAR'),
    dict(name=['-m', '--target'], help='Compile target MCU. Example: K64F, NUCLEO_F401RE, NRF51822...'),
    dict(name=['--profile'], action='append', help='Path of a build profile configuration file. Example: yos/tools/profiles/debug.json'),
    dict(name='--library', dest='compile_library', action='store_true', help='Compile the current program or library as a static library.'),
    dict(name='--config', dest='compile_config', action='store_true', help='Show run-time compile configuration'),
    dict(name='--prefix', dest='config_prefix', action='append', help='Restrict listing to parameters that have this prefix'),
    dict(name='--source', action='append', help='Source directory. Default: . (current dir)'),
    dict(name='--build', help='Build directory. Default: build/'),
    dict(name=['-c', '--clean'], action='store_true', help='Clean the build directory before compiling'),
    dict(name=['-N', '--artifact-name'], help='Name of the built program or library'),
    dict(name=['-S', '--supported'], dest='supported', action='store_true', help='Shows supported matrix of targets and toolchains'),
    dict(name='--app-config', dest="app_config", help="Path of an app configuration file (Default is to look for 'yos_app.json')"),
    help='Compile code using the yos build tools',
    description=("Compile this program using the yos build tools."))
def compile_(toolchain=None, target=None, profile=False, compile_library=False, compile_config=False, config_prefix=None, source=False, build=False, clean=False, artifact_name=None, supported=False, app_config=None):
    # Gather remaining arguments
    args = remainder
    # Find the root of the program
    program = Program(os.getcwd(), True)
    program.check_requirements(True)
    # Remember the original path. this is needed for compiling only the libraries and tests for the current folder.
    orig_path = os.getcwd()

    with cd(program.path):
        tools_dir = os.path.abspath(program.get_tools())

    # Prepare environment variables
    env = program.get_env()

    if not source or len(source) == 0:
        source = [os.path.relpath(program.path, orig_path)]

    if supported:
        popen(['python', '-u', os.path.join(tools_dir, 'make.py')]
              + (['-S'] if supported else []) + (['-v'] if very_verbose else [])
              + (['--app-config', app_config] if app_config else [])
              + args,
              env=env)
        return

    target = program.get_target(target)
    tchain = program.get_toolchain(toolchain)
    macros = program.get_macros()

    if compile_config:
        # Compile configuration
        popen(['python', os.path.join(tools_dir, 'get_config.py')]
              + ['-t', tchain, '-m', target]
              + list(chain.from_iterable(izip(repeat('--profile'), profile or [])))
              + list(chain.from_iterable(izip(repeat('--source'), source)))
              + (['-v'] if verbose else [])
              + (list(chain.from_iterable(izip(repeat('--prefix'), config_prefix))) if config_prefix else []),
              env=env)
    else:
        # If the user hasn't supplied a build directory, ignore the default build directory
        if not build:
            program.ignore_build_dir()
        
        build_path = build

        if compile_library:
            # Compile as a library (current dir is default)
            if not build_path:
                build_path = os.path.join(os.path.relpath(program.path, orig_path), program.build_dir, 'libraries', os.path.basename(orig_path), target, tchain)

            popen(['python', '-u', os.path.join(tools_dir, 'build.py')]
                  + list(chain.from_iterable(izip(repeat('-D'), macros)))
                  + ['-t', tchain, '-m', target]
                  + list(chain.from_iterable(izip(repeat('--profile'), profile or [])))
                  + list(chain.from_iterable(izip(repeat('--source'), source)))
                  + ['--build', build_path]
                  + (['-c'] if clean else [])
                  + (['--artifact-name', artifact_name] if artifact_name else [])
                  + (['-v'] if verbose else [])
                  + args,
                  env=env)
        else:
            # Compile as application (root is default)
            if not build_path:
                build_path = os.path.join(os.path.relpath(program.path, orig_path), program.build_dir, target, tchain)

            popen(['python', '-u', os.path.join(tools_dir, 'make.py')]
                  + list(chain.from_iterable(izip(repeat('-D'), macros)))
                  + ['-t', tchain, '-m', target]
                  + list(chain.from_iterable(izip(repeat('--profile'), profile or [])))
                  + list(chain.from_iterable(izip(repeat('--source'), source)))
                  + ['--build', build_path]
                  + (['-c'] if clean else [])
                  + (['--artifact-name', artifact_name] if artifact_name else [])
                  + (['--app-config', app_config] if app_config else [])
                  + (['-v'] if verbose else [])
                  + args,
                  env=env)

    program.set_defaults(target=target, toolchain=tchain)


# Test command
@subcommand('test',
    dict(name=['-t', '--toolchain'], help='Compile toolchain. Example: ARM, GCC_ARM, IAR'),
    dict(name=['-m', '--target'], help='Compile target MCU. Example: K64F, NUCLEO_F401RE, NRF51822...'),
    dict(name='--compile-list', dest='compile_list', action='store_true', help='List all tests that can be built'),
    dict(name='--run-list', dest='run_list', action='store_true', help='List all built tests that can be ran'),
    dict(name='--compile', dest='compile_only', action='store_true', help='Only compile tests'),
    dict(name='--run', dest='run_only', action='store_true', help='Only run tests'),
    dict(name=['-n', '--tests-by-name'], dest='tests_by_name', help='Limit the tests to a list (ex. test1,test2,test3)'),
    dict(name='--source', action='append', help='Source directory. Default: . (current dir)'),
    dict(name='--build', help='Build directory. Default: build/'),
    dict(name=['--profile'], action='append', help='Path of a build profile configuration file. Example: yos/tools/profiles/debug.json'),
    dict(name=['-c', '--clean'], action='store_true', help='Clean the build directory before compiling'),
    dict(name='--test-spec', dest="test_spec", help="Path used for the test spec file used when building and running tests (the default path is the build directory)"),
    dict(name='--app-config', dest="app_config", help="Path of an app configuration file (Default is to look for 'yos_app.json')"),
    help='Find, build and run tests',
    description=("Find, build, and run tests in a program and libraries"))
def test_(toolchain=None, target=None, compile_list=False, run_list=False, compile_only=False, run_only=False, tests_by_name=None, source=False, profile=False, build=False, clean=False, test_spec=None, app_config=None):
    # Gather remaining arguments
    args = remainder
    # Find the root of the program
    program = Program(os.getcwd(), True)
    program.check_requirements(True)
    # Save original working directory
    orig_path = os.getcwd()

    target = program.get_target(target)
    tchain = program.get_toolchain(toolchain)
    macros = program.get_macros()
    tools_dir = program.get_tools()
    build_and_run_tests = not compile_list and not run_list and not compile_only and not run_only

    # Prepare environment variables
    env = program.get_env()

    with cd(program.path):
        # Setup the source path if not specified
        if not source or len(source) == 0:
            source = [program.path]

        # Setup the build path if not specified
        build_path = build
        if not build_path:
            build_path = os.path.join(program.path, program.build_dir, 'tests', target, tchain)

        if test_spec:
            # Preserve path to given test spec
            test_spec = os.path.relpath(os.path.join(orig_path, test_spec), program.path)
        else:
            # Create the path to the test spec file
            test_spec = os.path.join(build_path, 'test_spec.json')

        if compile_list:
            popen(['python', '-u', os.path.join(tools_dir, 'test.py'), '--list']
                  + list(chain.from_iterable(izip(repeat('--profile'), profile or [])))
                  + ['-t', tchain, '-m', target]
                  + list(chain.from_iterable(izip(repeat('--source'), source)))
                  + (['-n', tests_by_name] if tests_by_name else [])
                  + (['-v'] if verbose else [])
                  + (['--app-config', app_config] if app_config else [])
                  + args,
                  env=env)

        if compile_only or build_and_run_tests:
            # If the user hasn't supplied a build directory, ignore the default build directory
            if not build:
                program.ignore_build_dir()

            popen(['python', '-u', os.path.join(tools_dir, 'test.py')]
                  + list(chain.from_iterable(izip(repeat('-D'), macros)))
                  + list(chain.from_iterable(izip(repeat('--profile'), profile or [])))
                  + ['-t', tchain, '-m', target]
                  + (['-c'] if clean else [])
                  + list(chain.from_iterable(izip(repeat('--source'), source)))
                  + ['--build', build_path]
                  + ['--test-spec', test_spec]
                  + (['-n', tests_by_name] if tests_by_name else [])
                  + (['-v'] if verbose else [])
                  + (['--app-config', app_config] if app_config else [])
                  + args,
                  env=env)

        if run_list:
            popen(['yosgt', '--test-spec', test_spec, '--list']
                  + (['-n', tests_by_name] if tests_by_name else [])
                  + (['-V'] if verbose else [])
                  + args,
                  env=env)

        if run_only or build_and_run_tests:
            popen(['yosgt', '--test-spec', test_spec]
                  + (['-n', tests_by_name] if tests_by_name else [])
                  + (['-V'] if verbose else [])
                  + args,
                  env=env)

    program.set_defaults(target=target, toolchain=tchain)


# Export command
@subcommand('export',
    dict(name=['-i', '--ide'], help='IDE to create project files for. Example: UVISION4, UVISION5, GCC_ARM, IAR, COIDE'),
    dict(name=['-m', '--target'], help='Export for target MCU. Example: K64F, NUCLEO_F401RE, NRF51822...'),
    dict(name='--source', action='append', help='Source directory. Default: . (current dir)'),
    dict(name=['-c', '--clean'], action='store_true', help='Clean the build directory before compiling'),
    dict(name=['-S', '--supported'], dest='supported', action='store_true', help='Shows supported matrix of targets and toolchains'),
    help='Generate an IDE project',
    description=(
        "Generate IDE project files for the current program."))
def export(ide=None, target=None, source=False, clean=False, supported=False):
    # Gather remaining arguments
    args = remainder
    # Find the root of the program
    program = Program(os.getcwd(), True)
    program.check_requirements(True)
    # Remember the original path. this is needed for compiling only the libraries and tests for the current folder.
    orig_path = os.getcwd()
    # Change directories to the program root to use yos OS tools
    with cd(program.path):
        tools_dir = program.get_tools()

    # Prepare environment variables
    env = program.get_env()

    if supported:
        popen(['python', '-u', os.path.join(tools_dir, 'project.py')]
              + (['-S'] if supported else []) + (['-v'] if very_verbose else []),
              env=env)
        return

    target = program.get_target(target)
    macros = program.get_macros()

    if not ide:
        error('Please specify ide using the -i switch')

    if not source or len(source) == 0:
        source = [os.path.relpath(program.path, orig_path)]
    
    program.ignore_build_dir()

    popen(['python', '-u', os.path.join(tools_dir, 'project.py')]
          + list(chain.from_iterable(izip(repeat('-D'), macros)))
          + ['-i', ide.lower()]
          + ['-m', target]
          + (['-c'] if clean else [])
          + list(chain.from_iterable(izip(repeat('--source'), source)))
          + args,
          env=env)

    program.set_defaults(target=target)


# Test command
@subcommand('detect',
    help='Detect connected yos targets/boards\n\n',
    description=(
        "Detects yos targets/boards connected to this system and shows supported\n"
        "toolchain matrix."))
def detect():
    # Gather remaining arguments
    args = remainder
    # Find the root of the program
    program = Program(os.getcwd(), False)
    program.check_requirements(True)
    # Change directories to the program root to use yos OS tools
    with cd(program.path):
        tools_dir = program.get_tools_dir()

    if tools_dir:
        # Prepare environment variables
        env = program.get_env()

        popen(['python', '-u', os.path.join(tools_dir, 'detect_targets.py')]
              + args,
              env=env)
    else:
        warning("The yos tools were not found in \"%s\". \nLimited information will be shown about connected yos targets/boards" % program.path)
        targets = program.get_detected_targets()
        if targets:
            for target in targets:
                action("Detected \"%s\" connected to \"%s\" and using com port \"%s\"" % (target['name'], target['mount'], target['serial']))
'''

# Make command
@subcommand('make',
    help='Make yos program/component',
    description=(
        "Make yos program/component."))
def make():
   # Get the make arguments
    make_args = ' '.join(sys.argv[2:])
    _run_make(['-f build/Makefile',make_args])

# Make command
@subcommand('makelib',
    dict(name='path', nargs='?', help='Library directory path.'),
    dict(name=['-N', '--new'], dest='new', action='store_true', help='Create a library configure makefile .'),
    help='Compile static library\n\n',
    description=(
        "Compile static library."))
def makelib(path, new=False):
    if new:
        root_dir = Program().path
        with open(os.path.join(root_dir,'yos/template/makefiles/yos_library_makefile/template.mk'), 'r') as f:
            content = f.read()
        with open(os.path.join(root_dir, path, os.path.basename(path)+'_src.mk'), 'w') as f:
            f.write(content.replace('template', os.path.basename(path)))
        return

    host_arch = ['Cortex-M3', 'Cortex-M4', 'Cortex-M4F', "ARM968E-S"]
    for arch in host_arch:
        _run_make(['LIB_DIR='+path, 'HOST_ARCH='+arch, '-f yos/makefiles/yos_library_makefile.mk'])

# Generic config command
@subcommand('config',
    dict(name='var', nargs='?', help='Variable name. E.g. "yosder", "protocol"'),
    dict(name='value', nargs='?', help='Value. Will show the currently set default value for a variable if not specified.'),
    dict(name=['-G', '--global'], dest='global_cfg', action='store_true', help='Use global settings, not local'),
    dict(name=['-U', '--unset'], dest='unset', action='store_true', help='Unset the specified variable.'),
    dict(name=['-L', '--list'], dest='list_config', action='store_true', help='List yos tool configuration.'),
    help='Tool configuration\n\n',
    description=(
        "Gets, sets or unsets yos tool configuration options.\n"
        "Options can be global (via the --global switch) or local (per program)\n"
        "Global options are always overridden by local/program options.\n"
        "Currently supported options: yosder, protocol, depth, cache"))
def config_(var=None, value=None, global_cfg=False, unset=False, list_config=False):
    name = var
    var = str(var).upper()

    if list_config:
        g = Global()
        g_vars = g.list_cfg().items()
        action("Global config:")
        if g_vars:
            for v in g_vars:
                log("%s=%s\n" % (v[0], v[1]))
        else:
            log("No global configuration is set\n")
        log("\n")

        p = Program(os.getcwd())
        action("Local config (%s):" % p.path)
        if not p.is_cwd:
            p_vars = p.list_cfg().items()
            if p_vars:
                for v in p_vars:
                    log("%s=%s\n" % (v[0], v[1]))
            else:
                log("No local configuration is set\n")
        else:
            log("Couldn't find valid yos program in %s\n" % p.path)

    elif name:
        if global_cfg:
            # Global configuration
            g = Global()
            if unset:
                g.set_cfg(var, None)
                action('Unset global %s' % name)
            elif value:
                g.set_cfg(var, value)
                action('%s now set as global %s' % (value, name))
            else:
                value = g.get_cfg(var)
                action(('%s' % value) if value else 'No global %s set' % (name))
        else:
            # Find the root of the program
            program = Program(os.getcwd())
            if program.is_cwd and not var == 'ROOT':
                error(
                    "Could not find yos program in current path \"%s\".\n"
                    "Change the current directory to a valid yos program, set the current directory as an yos program with 'yos config root .', or use the '--global' option to set global configuration." % program.path)
            with cd(program.path):
                if unset:
                    program.set_cfg(var, None)
                    action('Unset default %s in program "%s"' % (name, program.name))
                elif value:
                    program.set_cfg(var, value)
                    action('%s now set as default %s in program "%s"' % (value, name, program.name))
                else:
                    value = program.get_cfg(var)
                    action(('%s' % value) if value else 'No default %s set in program "%s"' % (name, program.name))
    else:
        subcommands['config'].error("too few arguments")


'''
# Build system and exporters
@subcommand('target',
    dict(name='name', nargs='?', help='Default target name. Example: K64F, NUCLEO_F401RE, NRF51822...'),
    dict(name=['-G', '--global'], dest='global_cfg', action='store_true', help='Use global settings, not local'),
    dict(name=['-S', '--supported'], dest='supported', action='store_true', help='Shows supported matrix of targets and toolchains'),
    help='Set or get default target',
    description=(
        "Set or get default toolchain\n"
        "This is an alias to 'yos config [--global] target [name]'\n"))
def target_(name=None, global_cfg=False, supported=False):
    if supported:
        return compile_(supported=supported)
    return config_('target', name, global_cfg=global_cfg)

@subcommand('toolchain',
    dict(name='name', nargs='?', help='Default toolchain name. Example: ARM, GCC_ARM, IAR'),
    dict(name=['-G', '--global'], dest='global_cfg', action='store_true', help='Use global settings, not local'),
    dict(name=['-S', '--supported'], dest='supported', action='store_true', help='Shows supported matrix of targets and toolchains'),
    help='Set or get default toolchain\n\n',
    description=(
        "Set or get default toolchain\n"
        "This is an alias to 'yos config [--global] toolchain [name]'\n"))
def toolchain_(name=None, global_cfg=False, supported=False):
    if supported:
        return compile_(supported=supported)
    return config_('toolchain', name, global_cfg=global_cfg)
'''
@subcommand('help',
    help='This help screen')
def help_():
    return parser.print_help()

def main():
    global verbose, very_verbose, remainder, cwd_root

    # Help messages adapt based on current dir
    cwd_root = os.getcwd()

    if sys.version_info[0] != 2 or sys.version_info[1] < 7:
        error(
            "yos cube is compatible with Python version >= 2.7 and < 3.0\n"
            "Please refer to the online guide available at https://code.aliyun.com/yos/yos-cube")

    # Parse/run command
    if len(sys.argv) <= 1:
        help_()
        sys.exit(1)

    if '--version' in sys.argv:
        log(ver+"\n")
        sys.exit(0)

    pargs, remainder = parser.parse_known_args()
    status = 1

    try:
        very_verbose = pargs.very_verbose
        verbose = very_verbose or pargs.verbose
        info('Working path \"%s\" (%s)' % (os.getcwd(), Repo.pathtype(cwd_root)))
        status = pargs.command(pargs)
    except ProcessException as e:
        error(
            "\"%s\" returned error code %d.\n"
            "Command \"%s\" in \"%s\"" % (e[1], e[0], e[2], e[3]), e[0])
    except OSError as e:
        if e[0] == errno.ENOENT:
            error(
                "Could not detect one of the command-line tools.\n"
                "You could retry the last command with \"-v\" flag for verbose output\n", e[0])
        else:
            error('OS Error: %s' % e[1], e[0])
    except KeyboardInterrupt as e:
        info('User aborted!', -1)
        sys.exit(255)
    except Exception as e:
        if very_verbose:
            traceback.print_exc(file=sys.stdout)
        error("Unknown Error: %s" % e, 255)
    sys.exit(status or 0)


if __name__ == "__main__":
    main()
