from tools.git import Git
from tools.package_management import apt_get, yum, zypper
from tools.utils import get_save_path, call
from config import Yocto as c
import subprocess
from os import mkdir, path
import re

def setup(yocto_path):
  yocto = Yocto(yocto_path)
  yocto.download()
  yocto.download_layer(c.meta_gumstix_repo, c.meta_gumstix_name)
  yocto.enter_build_environment()
  yocto.add_layer(c.meta_gumstix_name)
  yocto.set_machine(c.machine)

def get_dependencies(option):
  globals()[option+'_dependencies']()

def ubuntu_dependencies():
  apt_get.install(c.ubuntu_dependencies)

def fedora_dependencies():
  yum.groupinstall('development tools')
  yum.install(c.fedora_dependencies)

def opensuse_dependencies():
  zypper.install(c.opensuse_dependencies)

def centos_dependencies():
  yum.groupinstall('development tools', ['-y'])
  yum.install(c.centos_dependencies, ['-y'])


class Yocto():
  def __init__(self, directory):
    self.path = path.abspath(path.expanduser(directory))
  def download(self):
    git = Git(self.path)
    git.clone(c.oe_core_repo)
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
    self.set_option('MACHINE', machine, 'build/conf/local.conf')

  def add_to_option(self, option, append, file):
    self.re_file(path.join(self.path, 'build/conf/bblayers.conf'),
                 r'((?:.|[\n\r])*' + option + r' *?\??\??= *?"(?:.|[\n\r])*?)("(?:.|[\n\r])*)',
                 r'\1 ' + append + r'\2')
  def set_option(self, option, value, file):
    self.re_file(path.join(self.path, file),
                 r'((?:.|[\n\r])*\n *' + option + r') *?\??\??= *?".*?"((?:.|[\n\r])*)',
                 r'\1 = "'+ value + r'"\2')
  def re_file(self, file, pattern, replace):
    source = open(file).read()
    output = open(file, 'w')
    output.write(re.sub(pattern, replace, source))
    output.close()
