import os
import shutil
from .errors import *

def make_executable(path):
    mode = os.stat(path).st_mode
    mode |= (mode & 0o444) >> 2    # copy R bits to X
    os.chmod(path, mode)

def get_symlink_target(path):
    dirpath = os.path.dirname(os.path.abspath(path))
    return os.path.join(dirpath, os.readlink(path))

def move_file(src, dst):
    if os.path.isdir(dst):
        raise DirectoryExistsError(dst)
    shutil.move(src, dst)
