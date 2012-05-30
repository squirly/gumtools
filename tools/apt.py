from tools.utils import sudo_call

class apt_get():   
  @staticmethod 
  def install(packages):
    packages.insert(0, 'install')
    sudo_call('apt-get', packages)
