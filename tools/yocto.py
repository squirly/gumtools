from tools.git import Git
from tools.apt import apt_get
from tools.utils import get_save_path, call
import subprocess
from os import mkdir, path
import re

def setup(yocto_path):
  get_dependencies()
  yocto = Yocto(yocto_path)
  yocto.download()
  yocto.download_layer('git@github.com:squirly/gumtools.git', 'meta-gumstix')
  yocto.enter_build_environment()
  yocto.add_layer('meta-gumstix')
  yocto.set_machine('overo')

def get_dependencies():
  apt_get.install(['sed', 'wget', 'subversion', 'git-core', 'coreutils', 'unzip', 'texi2html', 'texinfo', 'libsdl1.2-dev', 'docbook-utils', 'fop', 'gawk', 'python-pysqlite2', 'diffstat', 'make', 'gcc', 'build-essential', 'xsltproc', 'g++', 'desktop-file-utils', 'chrpath', 'libgl1-mesa-dev', 'libglu1-mesa-dev', 'autoconf', 'automake', 'groff', 'libtool', 'xterm', 'libxml-parser-perl'])

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
