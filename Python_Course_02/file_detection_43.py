import os

path = 'test.txt'

if os.path.exists(path):
    print('Yes!')
    if os.path.isfile(path):
        print('It is a file!')
    elif os.path.isdir(path):
        print('It is a directory!')
else:
    print('No!')
