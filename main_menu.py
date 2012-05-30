from tools import sdcard
from tools.menu import Menu, MenuItem
from tools.prompt import ask_yes_no
from flash.standard import Standard
from tools.command_line import CommandLine
from tools.utils import get_save_path
from os import path
import os

INSTALL = 'install'
YOCTO = 'yocto'

m = Menu()
m.query = 'Please choose a task'
m.items.append(MenuItem('Install a distro to Micro SD', INSTALL))
m.items.append(MenuItem('Setup the image build environment', YOCTO))
m.items.append(MenuItem('Exit', ''))
option = m.show()
if option == INSTALL:
  if not os.geteuid()==0:
		exit("You must be root to run this action, please use sudo and try again.")
  import distros
  while True:
    distro = distros.select()
    if CommandLine.peek_next():
      break
    print distro.get_description()
    print 'There is an option to download this distro' if distro.can_download() else 'You must have already downloaded an image in order to install this distro.'
    print '\n',
    if ask_yes_no('Would you like to install ' + distro.get_name() + '?', True):
      break
  distro.install(sdcard.select_card())
elif option == YOCTO:
  from tools import yocto
  yocto.setup(path.join(get_save_path(), 'yocto'))
