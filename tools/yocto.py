from tools.git import Git
from tools.package_management import apt_get, yum, zypper
from tools.utils import get_save_path, call
import subprocess
from os import mkdir, path
import re

def setup(yocto_path):
  yocto = Yocto(yocto_path)
  yocto.download()
  yocto.download_layer('git@github.com:squirly/meta-gumstix.git', 'meta-gumstix')
  yocto.enter_build_environment()
  yocto.add_layer('meta-gumstix')
  yocto.set_machine('overo')

def get_dependencies(option):
  globals()[option+'_dependencies']()

def ubuntu_dependencies():
  apt_get.install(['sed', 'wget', 'subversion', 'git-core', 'coreutils', 'unzip', 'texi2html', 'texinfo', 'libsdl1.2-dev', 'docbook-utils', 'fop', 'gawk', 'python-pysqlite2', 'diffstat', 'make', 'gcc', 'build-essential', 'xsltproc', 'g++', 'desktop-file-utils', 'chrpath', 'libgl1-mesa-dev', 'libglu1-mesa-dev', 'autoconf', 'automake', 'groff', 'libtool', 'xterm', 'libxml-parser-perl'])

def fedora_dependencies():
  yum.groupinstall('development tools')
  yum.install(['python', 'm4', 'make', 'wget', 'curl', 'ftp', 'tar', 'bzip2', 'gzip', 'unzip', 'perl', 'texinfo', 'texi2html', 'diffstat', 'openjade', 'docbook-style-dsssl', 'sed', 'docbook-style-xsl', 'docbook-dtds', 'fop', 'xsltproc', 'docbook-utils', 'sed', 'bc', 'eglibc-devel', 'ccache', 'pcre', 'pcre-devel', 'quilt', 'groff', 'linuxdoc-tools', 'patch', 'cmake', 'perl-ExtUtils-MakeMaker', 'tcl-devel', 'gettext', 'chrpath', 'ncurses', 'apr', 'SDL-devel', 'mesa-libGL-devel', 'mesa-libGLU-devel', 'gnome-doc-utils', 'autoconf', 'automake', 'libtool', 'xterm'])

def opensuse_dependencies():
  zypper.install(['python', 'gcc', 'gcc-c++', 'libtool', 'fop', 'subversion', 'git', 'chrpath', 'automake', 'make', 'wget', 'xsltproc', 'diffstat', 'texinfo', 'freeglut-devel', 'libSDL-devel'])

def centos_dependencies():
  yum.groupinstall('development tools', ['-y'])
  yum.install(['tetex', 'gawk', 'sqlite-devel', 'vim-common', 'redhat-lsb', 'xz', 'm4', 'make', 'wget', 'curl', 'ftp', 'tar', 'bzip2', 'gzip', 'python-devel', 'unzip', 'perl', 'texinfo', 'texi2html', 'diffstat', 'openjade', 'zlib-devel', 'docbook-style-dsssl', 'sed', 'docbook-style-xsl', 'docbook-dtds', 'docbook-utils', 'bc', 'glibc-devel', 'pcre', 'pcre-devel', 'groff', 'linuxdoc-tools', 'patch', 'cmake', 'tcl-devel', 'gettext', 'ncurses', 'apr', 'SDL-devel', 'mesa-libGL-devel', 'mesa-libGLU-devel', 'gnome-doc-utils', 'autoconf', 'automake', 'libtool', 'xterm'], ['-y'])


class Yocto():
  def __init__(self, directory):
    self.path = path.abspath(path.expanduser(directory))
  def download(self):
    git = Git(self.path)
    git.clone('git://git.yoctoproject.org/poky.git')
  def download_layer(self, repo, name):
    git = Git(path.join(self.path, name))
    git.clone(repo)
  def enter_build_environment(self):
    call('cd', [self.path])
    command = ['bash', '-c', 'cd "'+self.path+'";source oe-init-build-env']
    proc = subprocess.Popen(command, stdout = subprocess.PIPE)
    proc.communicate()

  def add_layer(self, name):
    self.add_to_option('BBLAYERS', path.join(self.path, name), 'build/conf/bblayers.conf');
  def set_machine(self, machine):
    self.set_option('MACHINE', machine, 'build/conf/bblayers.conf')

  def add_to_option(self, option, append, file):
    self.re_file(path.join(self.path, 'build/conf/bblayers.conf'),
                 r'((?:.|[\n\r])*' + option + r' *?\??\??= *?"(?:.|[\n\r])*?)("(?:.|[\n\r])*)',
                 r'\1 '+append+r'\2')
  def set_option(self, option, value, file):
    self.re_file(path.join(self.path, file),
                 r'((?:.|[\n\r])*\n *' + option + r') *?\??\??= *?".*?"((?:.|[\n\r])*)',
                 r'\1 = "'+ value +r'"\2')
  def re_file(self, file, pattern, replace):
    source = open(file).read()
    output = open(file, 'w')
    output.write(re.sub(pattern, replace, source))
    output.close()
