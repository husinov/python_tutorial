import os

source = 'folderr'
destination = 'C:\\Users\\Nuriddin Husinov\\Desktop\\folder'

try:
    if os.path.exists(destination):
        print('There is a file!')
    else:
        print('Work is done!')
except FileNotFoundError:
    print('No file in this location!')
