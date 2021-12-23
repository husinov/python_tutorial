# import os
# import shutil

from os import remove, rmdir
from shutil import rmtree
path = 'test.txt'

try:
    # os.remove(path)     #delete a file
    remove(path)
    # os.rmdir(path)      #delete an empty directory
    rmdir(path)
    # shutil.rmtree(path) #delete a diretory containing files
    rmtree(path)
except FileNotFoundError:
    print('File was not found!')
except PermissionError:
    print('You chose the wrong function!')
except OSError:
    print('Empty directory or work with shutil module!')
else:
    print('Work is done!')
