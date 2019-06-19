import shutil
import os
import datetime as dt
import time

# A to B directory
from_dir = os.path.join(os.environ['HOMEPATH'], 'DESKTOP', 'A')
to_dir = os.path.join(os.environ['HOMEPATH'], 'DESKTOP', 'B')
dir = os.listdir(from_dir)
delim = '\\'
filepath = []

def transferFiles():

    trans = 0
    for f in dir:
        filepath.append(f)

    for file in filepath:
        print(file)

    t = dt.datetime.strptime(time.ctime(),'%a %b %d %H:%M:%S %Y')
    currday = t.strftime('%Y-%m-%d')
    for f in filepath:
        mod = time.strftime('%Y-%m-%d', time.gmtime(os.path.getmtime(from_dir+delim+f)))
        if mod == currday:
            shutil.copy(from_dir+delim+f, to_dir)

    print('%i files transferred.' %trans)

transferFiles()