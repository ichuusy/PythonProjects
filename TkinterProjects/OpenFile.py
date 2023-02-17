from tkinter import *
from tkinter import filedialog,messagebox
import os

gui = Tk()
check = False
path = None
def GetPath():
    global path
    path = filedialog.askopenfile().name
    messagebox.showinfo("Dosya yolu bulundu",f"{path}")
    if(path != None):
        check = True
    if(check):
        Button(gui,text="Programı başlat",command=RunProgram).grid(row=3,column=0,sticky=N)
def RunProgram():
    os.system(path)
    messagebox.showwarning("Uygulama başlatıldı",f"Başlatılan uygulamanın dosya yolu {path}")
Label(gui,text="Bir dosyanın dosya yolunu öğrenmek için butona tıkla.").grid(row=1,column=0,sticky=W)
Button(gui,text="Dosya Seç",command=GetPath).grid(row=2,column=0,sticky=N)

gui.mainloop()