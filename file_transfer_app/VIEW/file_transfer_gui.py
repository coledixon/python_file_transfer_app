from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import filedialog as fd
# CUSTOM SCRIPTS
from CONTROLLER import file_transfer_controller as ctrl
from CONTROLLER import file_transfer_data as data

class FileTransfer:

    def __init__(self, master):

        # DEFINE GLOBALS
        self.chk = BooleanVar()

        # MASTER SETTINGS
        self.master = master
        self.master.minsize(500, 200)
        self.master.maxsize(500, 200)
        self.master.title('FILE TRANSFER')
        self.master.resizable(False, False)
        self.master.configure(background = 'light blue')

        # FORM FIELDS
        self.file_entry = Entry(self.master, text='', width=52)
        self.file_entry.grid(row=1, column=1, padx=(25, 0), pady=(50, 0), sticky=NW)
        self.file_dest = Entry(self.master, text='', width=52)
        self.file_dest.grid(row=2, column=1, padx=(25, 0), pady=(10, 0), sticky=NW)

        # FORM BUTTONS
        self.btnRoot = Button(self.master, text='BROWSE ROOT', width=15, height=1)
        self.btnRoot.grid(row=1, column=0, padx=(20, 0), pady=(50, 0))
        self.btnDest = Button(self.master, text='BROWSE DEST', width=15, height=1)
        self.btnDest.grid(row=2, column=0, padx=(20, 0), pady=(10, 0))
        self.btnTransfer = Button(self.master, text='TRANSFER', width=15, height=3)
        self.btnTransfer.grid(row=3, column=0, padx=(20, 0), pady=(10, 0))
        self.btnClear = Button(self.master, text='CLEAR', width=15, height=3)
        self.btnClear.grid(row=3, column=1, padx=(20, 0), pady=(10, 0), sticky=E)

        # BIND BUTTON EVENTS
        self.btnTransfer.bind('<1>', lambda e: ctrl.transfer_(self))
        self.btnClear.bind('<1>', lambda e: ctrl.clear_(self))
        self.btnRoot.bind('<1>', lambda e: ctrl.browseRoot_(self))
        self.btnDest.bind('<1>', lambda e: ctrl.browseDest_(self))

        # FORM PROGRESS BAR
        self.prog = ttk.Progressbar(master, orient=HORIZONTAL, length=455, mode='determinate')
        self.prog.grid(row=0, column=1, pady=(30, 10))
        self.prog.place(relx=0.5, rely=0.1, anchor='c')

        # FORM CHECKBUTTON
        self.check = ttk.Checkbutton(master, text="MOVE ALL FILES", onvalue=1, offvalue=0, variable=self.chk)
        self.check.grid(row=3, column=0)
        self.check.place(relx=0.4, rely=0.65, anchor='c')
