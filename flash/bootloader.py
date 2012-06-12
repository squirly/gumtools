from os import path
from tools.utils import http_download, get_temp_path, clear_dir
from config import Bootloader as c

def setup(sdcard):
	aquire()
	copy(sdcard)

def aquire():
	temp = get_temp_path()
	for com_file, serv_file in c.files.items():
		if not path.isfile(path.join(temp, com_file)):
			http_download(path.join(c.server, serv_file), path.join(temp, com_file))

def copy(sdcard):
	clear_dir(sdcard.boot_dir)
	temp = get_temp_path()
	for file in files:
		sdcard.copy_to_boot(path.join(temp, file))
