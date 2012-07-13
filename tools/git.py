from tools.utils import call
from os import path

class Git():
  def __init__(self, directory):
    self.base_path = path.abspath(path.expanduser(directory))

  def git_call(self, function, args):
   args = ["--git-dir=" + path.join(self.base_path, '.git'), "--work-tree=" + self.base_path, function] + args
   call('git', args)

  def clone(self, repo):
    params = [repo]
    params.append(self.base_path)
    params.insert(0, 'clone')
    call('git', params)

  def checkout(self, branch):
    self.git_call('checkout', [branch])
