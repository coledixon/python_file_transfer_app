from tkinter import *
from tkinter import ttk
# CUSTOM SCRIPTS
from VIEW import file_transfer_gui as gui
from MODEL import file_transfer_init_schema as schema

# MAIN APPLICATION
def main():
    root = Tk()
    FT = gui.FileTransfer(root) # main app GUI
    schema.createDb() # create / init SQLite objects
    root.mainloop() # run app

if __name__ == '__main__': main()