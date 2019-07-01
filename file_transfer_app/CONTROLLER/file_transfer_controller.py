from tkinter import messagebox as mb
from tkinter import filedialog as fd
import shutil, os
import sqlite3 as sql
import datetime, time
# CUSTOM SCRIPTS
from CONTROLLER import file_transfer_data as data


# DEFINE GLOBALS
global path
global dest
global chk
global dirname


# BUTTON EVENTS
def browseRoot_(self):
    res = evalCheckState_(self)
    if res != False: # dynamically set functionality based on 'MOVE ALL' checkbutton
        dirname = fd.askdirectory()
    else:
        dirname = fd.askopenfilename()
    self.file_entry.delete(0, 'end')
    self.file_entry.insert(0, dirname)

def browseDest_(self):
    destname = fd.askdirectory()
    self.file_dest.delete(0, 'end')
    self.file_dest.insert(0, destname)

def clear_(self):
    self.file_entry.delete(0,'end')
    self.file_dest.delete(0,'end')

# CORE METHODS
def transfer_(self):
    chk = self.chk.get()
    path = self.file_entry.get()
    dest = self.file_dest.get()
    res = evalPaths_(path, dest)
    if chk != False:
        transferAll_(self, path, dest)
    else:
        if res != False:
            shutil.copy(path, dest)
            data.insertTran_(self, path, dest, os, datetime, time)
            clear_(self)
            mb.showinfo(title='FILE TRANSFER', message='File transferred to %s' %dest)

def transferAll_(self, p, d):
    p = parseToRoot_(self, p)
    res = evalPaths_(p, d)
    if res != False:
        dircontents = os.listdir(p)
        for f in dircontents:
            shutil.move(p+ '\\' +f, d)
            clear_(self)

# DEFINE HELPERS
def evalPaths_(p, d):
    if not p:
        mb.showerror(title="ERROR", message="ROOT CANNOT BE NULL")
        return False
    elif not d:
        mb.showerror(title="ERROR", message="DEST CANNOT BE NULL")
        return False
    elif p == d:
        mb.showerror(title="ERROR", message="ROOT AND DEST CANNOT BE THE SAME PATH")
        return False
    else:
        return True

def evalCheckState_(self):
    chk = self.chk.get()
    if chk == True:
        return True
    else:
        return False

def parseToRoot_(self, p):
    # if 'MOVE ALL' is checked and single file is selected, parse to root
    if '.' in p: # '.' indicates a file / not a root dir
        p = os.path.dirname(p) # parse to root
        self.file_dest.delete(0, 'end')
        self.file_dest.insert(0, p)
        return p



# def insertFile_(self):
#     evalPaths_(path, dest)
#     # path = self.file_entry.get()
#     # dest = self.file_dest.get()
#     type = os.path.splitext(self.file_entry.get())[1]
#     TransID = 0
#     FileID = 0
#     self.c.execute("INSERT INTO FileInfo VALUES(?,?,?,?,?)",
#                 (FileID, path, newpath, type, TransID))
#     self.conn.commit()

# def lastTransfer_(self):
#     timeran = time.clock()
#     print(timeran)
