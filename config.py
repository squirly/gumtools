
class Yocto:
  machine = 'overo'

  oe_core_repo = 'git://git.yoctoproject.org/poky.git'

  meta_gumstix_name = 'meta-gumstix'
  meta_gumstix_repo = 'git://github.com/squirly/meta-gumstix.git'

  package_type = 'package_deb'

  ubuntu_dependencies = ['sed', 'wget', 'subversion', 'git-core', 'coreutils', 'unzip', 'texi2html', 'texinfo', 'libsdl1.2-dev', 'docbook-utils', 'fop', 'gawk', 'python-pysqlite2', 'diffstat', 'make', 'gcc', 'build-essential', 'xsltproc', 'g++', 'desktop-file-utils', 'chrpath', 'libgl1-mesa-dev', 'libglu1-mesa-dev', 'autoconf', 'automake', 'groff', 'libtool', 'xterm', 'libxml-parser-perl']
  fedora_dependencies = ['python', 'm4', 'make', 'wget', 'curl', 'ftp', 'tar', 'bzip2', 'gzip', 'unzip', 'perl', 'texinfo', 'texi2html', 'diffstat', 'openjade', 'docbook-style-dsssl', 'sed', 'docbook-style-xsl', 'docbook-dtds', 'fop', 'xsltproc', 'docbook-utils', 'sed', 'bc', 'eglibc-devel', 'ccache', 'pcre', 'pcre-devel', 'quilt', 'groff', 'linuxdoc-tools', 'patch', 'cmake', 'perl-ExtUtils-MakeMaker', 'tcl-devel', 'gettext', 'chrpath', 'ncurses', 'apr', 'SDL-devel', 'mesa-libGL-devel', 'mesa-libGLU-devel', 'gnome-doc-utils', 'autoconf', 'automake', 'libtool', 'xterm']
  opensuse_dependencies = ['python', 'gcc', 'gcc-c++', 'libtool', 'fop', 'subversion', 'git', 'chrpath', 'automake', 'make', 'wget', 'xsltproc', 'diffstat', 'texinfo', 'freeglut-devel', 'libSDL-devel']
  centos_dependencies = ['tetex', 'gawk', 'sqlite-devel', 'vim-common', 'redhat-lsb', 'xz', 'm4', 'make', 'wget', 'curl', 'ftp', 'tar', 'bzip2', 'gzip', 'python-devel', 'unzip', 'perl', 'texinfo', 'texi2html', 'diffstat', 'openjade', 'zlib-devel', 'docbook-style-dsssl', 'sed', 'docbook-style-xsl', 'docbook-dtds', 'docbook-utils', 'bc', 'glibc-devel', 'pcre', 'pcre-devel', 'groff', 'linuxdoc-tools', 'patch', 'cmake', 'tcl-devel', 'gettext', 'ncurses', 'apr', 'SDL-devel', 'mesa-libGL-devel', 'mesa-libGLU-devel', 'gnome-doc-utils', 'autoconf', 'automake', 'libtool', 'xterm']

class Bootloader:
  server = 'http://cumulus.gumstix.org/images/angstrom/factory/2011-08-30-1058/'
  files = {
	  'MLO':'mlo-updated',
	  'u-boot.bin':'u-boot.bin',
  }
