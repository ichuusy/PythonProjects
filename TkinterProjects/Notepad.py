import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext,filedialog

gui = tk.Tk()
path = None

def SaveInfo():
    text = area.get("1.0",tk.END)
    global path
    name = None
    if(path == None):
        name = "notepad.txt"
    else:
        name = path
    fl = open(name, "w")
    fl.write(text)
    fl.close()

def OpenFile():
    global path
    get_path = filedialog.askopenfile()
    fl = open(f"{get_path.name}","r")
    text = area.insert(tk.INSERT,fl.read())
    path = get_path.name
    fl.close()

area = scrolledtext.ScrolledText(gui,wrap=tk.WORD)
tk.Button(gui,text="Kaydet",command=SaveInfo).grid(row=0,column=0,sticky=tk.W)
tk.Button(gui,text="Aç",command=OpenFile).grid(row=0,column=1,sticky=tk.W)
area.grid(row=5,column=1,sticky=tk.N)
gui.mainloop()