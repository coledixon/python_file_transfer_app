import shutil
import os

# A to B directory
from_dir = os.path.join(os.environ['HOMEPATH'], 'DESKTOP', 'A')
to_dir = os.path.join(os.environ['HOMEPATH'], 'DESKTOP', 'B')
# get contents of directory
dir_contents = os.listdir(from_dir)
files = []

# get files in directory / append to list
def fileDir():

    for f in dir_contents:
        files.append(f)

    count = len(files)
    print(count.__str__()+' files located at '+from_dir)
    for file in files:
        print(file)

# read contents of each file
def readFile():

    for i in files:
        from_dir+i
        f = open(from_dir+'\\'+i, 'r')
        for line in f:
            print('contents of '+i+': '+line)

# copy files A to B
def copyFile():

    for i in files:
        shutil.copy(from_dir+'\\'+i, to_dir)

fileDir()
readFile()
copyFile()
