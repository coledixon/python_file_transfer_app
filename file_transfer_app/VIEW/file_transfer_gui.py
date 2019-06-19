from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import filedialog as fd
# CUSTOM SCRIPTS
from CONTROLLER import file_transfer_controller as ctrl
from CONTROLLER import file_transfer_data as data

class FileTransfer:

    def __init__(self, master):

        # MASTER SETTINGS
        master.title('FILE TRANSFER')
        master.resizable(False, False)
        master.configure(background = 'black')

        self.style = ttk.Style()
        # IMAGE
        # CD REMOVED: self.transfer = PhotoImage(file = 'C:\\Users\\Dell 0381\\Desktop\\Python practice\\Custom Projects\\icons\\transfer.png')
        # CD REMOVED: self.icon = self.transfer


        # HEADER
        self.header_frame = ttk.Frame(master)
        self.header_frame.pack()

        # CD REMOVED: , image = self.icon
        ttk.Label(self.header_frame).grid(row = 0, column = 0, rowspan = 2)
        ttk.Label(self.header_frame, text = 'A SIMPLE FILE TRANSFER PROGRAM').grid(row = 0, column = 1)
        ttk.Label(self.header_frame, text = 'BROWSE for ROOT and DEST file locations.\n'
                                            'Apply COMMENTS as needed (or required).\n').grid(row = 1, column = 1)


        # CONTENT
        self.content = ttk.Frame(master)
        self.content.pack()

        ttk.Label(self.content, text = 'ROOT FILE PATH',font = ('sys', 10,'bold italic')).grid(row = 0, column = 0, padx = 5, sticky = 'nw')
        ttk.Label(self.content, text = 'DEST FILE PATH', font = ('sys', 10,'bold italic')).grid(row = 0, column = 1, padx = 5, sticky = 'nw')
        ttk.Label(self.content, text = 'COMMENTS', font = ('sys', 10,'bold italic')).grid(row = 3, column = 0, sticky = 'nw', padx = 100)


        # ENTRY FIELDS
        self.file_entry = ttk.Entry(self.content, width = 45, font = ('Ariel', 8))
        self.file_entry.grid(row = 1, column = 0, padx = 5)
        self.file_dest = ttk.Entry(self.content, width = 45, font = ('Ariel', 8))
        self.file_dest.grid(row = 1, column = 1, padx = 5)
        self.comments = Text(self.content, width = 50, height = 5)
        self.comments.grid(row = 4, column = 0, columnspan = 2)


        # BUTTONS
        self.btnRoot = ttk.Button(self.content, text = 'BROWSE')
        self.btnRoot.grid(row = 2, column = 0, sticky = 'nw', padx = 5, pady = 4)
        self.btnDest = ttk.Button(self.content, text = 'BROWSE')
        self.btnDest.grid(row = 2, column = 1, sticky = 'nw', padx = 5, pady = 4)
        self.btnClear = ttk.Button(self.content, text = 'CLEAR')
        self.btnClear.grid(row = 5, column = 0, sticky = 'sw',pady = 5, padx = 5)
        self.btnTransfer = ttk.Button(self.content, text = 'TRANSFER')
        self.btnTransfer.grid(row = 5, column = 1, sticky = 'ne', padx = 84, pady = 5)
        self.btnCancel = ttk.Button(self.content, text = 'CANCEL', command = quit).grid(row = 5, column = 1, sticky = 'ne', pady = 5, padx = 5)


        # PROGRESS BAR
        value = IntVar()
        self.prog = ttk.Progressbar(self.content, orient = HORIZONTAL, length = 250, maximum = 50.0, value = 0)
        #self.prog.grid(row = 4, column = 1)

        # BIND BUTTON EVENTS
        self.btnTransfer.bind('<1>', lambda e: ctrl.transfer_(self))
        self.btnClear.bind('<1>', lambda e: ctrl.clear_(self))
        self.btnRoot.bind('<1>', lambda e: ctrl.browseRoot_(self))
        self.btnDest.bind('<1>', lambda e: ctrl.browseDest_(self))
