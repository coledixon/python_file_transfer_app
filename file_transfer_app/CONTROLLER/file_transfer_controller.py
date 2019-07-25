from tkinter import messagebox as mb
from tkinter import filedialog as fd
import shutil, os
import sqlite3 as sql
import datetime, time
# CUSTOM SCRIPTS
from CONTROLLER import file_transfer_data as data


# DEFINE GLOBALS
path = ""
dest = ""
dirname = ""


# BUTTON EVENTS
def browseRoot_(self):
    # CD REMOVED: res = evalCheckState_(self)
    global dirname
    if evalCheckState_(self) != False: # dynamically set functionality based on 'MOVE ALL' checkbutton
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
    # CD REMOVED: chk = self.chk.get()
    global path 
    path = self.file_entry.get() # CD debug: global
    global dest 
    dest = self.file_dest.get() # CD debug: global

    # CD REMOVED: res = evalPaths_(path, dest)
    if self.chk.get() != False:
        transferAll_(self, path, dest)
    else:
        if evalPaths_(path, dest) != False: # CD debug: pass self.file_entry/dest.get() direct to method???
            startProgressbar_(self)
            shutil.move(path, dest)
            step = int(100 / len(dircontents))
            setProgress_(self, step)
            # data.insertTran_(self, path, dest, os, datetime, time)
            clear_(self)
            stopProgressbar_(self)
            mb.showinfo(title='FILE TRANSFER', message='File transferred to %s' %dest)

def transferAll_(self, p, d):
    global path 
    path = parseToRoot_(self, p)
    # CD REMOVED: res = evalPaths_(p, d)
    if evalPaths_(p,d) != False:
        dircontents = os.listdir(p)
        if evalDirContents_(self, len(dircontents)) == False:
            return None
        base = int(100 / len(dircontents)) # control val for incrementing progress
        step = base # step val
        startProgressbar_(self)
        for f in dircontents:
            shutil.move(p+ '\\' +f, d)
            setProgress_(self, step)
            if step < 100: # max determinate val for progressbar
                step = int(step + base) # increment progress step val
        clear_(self)
        stopProgressbar_(self)
        mb.showinfo(title='FILE TRANSFER', message='File transferred to %s' %d)

# PROGRESS BAR CONTROL(S)
def startProgressbar_(self):
    self.prog.start()

def stopProgressbar_(self):
    self.prog.stop()

def setProgress_(self, step):
    self.prog.step(step)
    time.sleep(1)
    self.prog.update_idletasks()

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
    # CD REMOVED: chk = self.chk.get()
    if self.chk.get() == True:
        return True
    else:
        return False

def evalDirContents_(self, cont):
    if cont == 0:
        mb.showinfo(title='FILE TRANSFER', message='No files to move in specified location')
        clear_(self)
        return False # abort method if no files to relocate

def parseToRoot_(self, p):
    # if 'MOVE ALL' is checked and single file is selected, parse to root
    if '.' in p: # '.' indicates a file / not a root dir
        p = os.path.dirname(p) # parse to root
        self.file_dest.delete(0, 'end')
        self.file_dest.insert(0, p)
        return p
    else:
        return p
