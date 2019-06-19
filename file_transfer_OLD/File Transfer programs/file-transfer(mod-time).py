import os
import datetime as dt
import shutil

def copyFile(src, dst):
    now = dt.datetime.now()
    ago = now-dt.timedelta(minutes=60)

    for file in os.listdir(src):
         full_path = os.path.join(src, file)
         st = os.stat(full_path)
         mtime = dt.datetime.fromtimestamp(st.st_mtime)
         if mtime > ago:
            shutil.copy(full_path, dst)
            print('%s modified %s'%(src +file, mtime))

copyFile("C:\\Users\\Dell 0381\\Desktop\\A\\", "C:\\Users\\Dell 0381\\Desktop\\B")