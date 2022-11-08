from urllib.request import *
from tkinter import *
from tkinter.filedialog import *

def browse():
    global path
    path['text'] = askdirectory()

def make_gui():
    global tk, path
    tk = Tk()
    Label(tk, text='Path:').grid(row=0, column=0)
    path = Label(tk, text='')
    path.grid(row=0, column=1)
    Button(tk, text='Browse', command=browse).grid(row=0, column=1)
    Button(tk, text='Install', command=browse).grid(row=1, column=1, columnspan=3, sticky='ew')

make_gui()
tk.mainloop()
