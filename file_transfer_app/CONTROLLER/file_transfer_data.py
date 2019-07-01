from tkinter import messagebox as mb
import sqlite3 as sql
# CUSTOM SCRIPTS
from CONTROLLER import file_transfer_controller as ctrl


# DEFINE GLOBALS
global conn
global transId
global success


# DEFINE DATABASE CONNECTION
def connectDb():
    try:
        conn = sql.connect('file_transfer.db') # db created on app load (app_main.py)
        return conn
    except sql.Error as e:
        mb.showinfo(title='ERROR', message='SQLite error on db connection file_transfer_data.connectDb(): ' + e.args[0])
 
    return None


# DATA EVENTS
def insertTran_(self, path, dest, os, datetime, time):
    conn = connectDb() # establish SQLite3 db conn
    cur = conn.cursor()
    data = [time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(os.path.getmtime(path))),
            datetime.datetime.strptime(time.ctime(),'%a %b %d %H:%M:%S %Y')]
    transId = 0
    for i in data:
        transId +=1
        try:
            cur.execute("INSERT INTO file_transfer VALUES(?,?,?,?)",
                    (transId, i, i, self.comments.get(1.0,'end')))
            conn.commit()
            insertFile_(self, path, dest, os)
        except sql.Error as e:
            mb.showinfo(title='ERROR', message='SQLite error in file_transfer_data.insertTran_(): ' + e.args[0])

def insertFile_(self, path, dest, os):
    conn = connectDb() # establish SQLite3 db conn
    cur = conn.cursor()
    type = os.path.splitext(self.file_entry.get())[1]
    tranId = 0
    fileId = 0
    cur.execute("INSERT INTO file_info VALUES(?,?,?,?,?)",
                (fileId, path, dest, type, tranId))
    conn.commit()

def selectLastTranIds():
    conn = connectDb() # establish SQLite3 db conn
    cur = conn.cursor()
    tranId = cur.execute("SELECT COALESE(MAX(tranId),0) FROM file_transfer")
    conn.commit()

def lastTransfer_(self):
    timeran = time.clock()
    print(timeran)