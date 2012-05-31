from tools.utils import sudo_call

class apt_get():
  @staticmethod 
  def install(packages):
    packages.insert(0, 'install')
    sudo_call('apt-get', packages)

class yum():
  @staticmethod
  def install(packages, extra=[]):
    packages.insert(0, 'install')
    sudo_call('yum', extra + packages)
  @staticmethod
  def groupinstall(group, extra=[]):
    extra += ['groupinstall', group]
    sudo_call('yum', extra)

class zypper():
  @staticmethod
  def install(packages):
    packages.insert(0, 'install')
    sudo_call('zypper', packages)
