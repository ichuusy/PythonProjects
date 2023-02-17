from tkinter import *
from tkinter import colorchooser,messagebox

gui = Tk()
Label(text="Renk seçmek için butona tıklayın.").grid(row=1,column=0,sticky=W) # Row 1, Column 0
def Color():
    color = colorchooser.askcolor()
    messagebox.showinfo(f"Renk seçimi başarılı",f"Seçilen renk : {color}")
Button(text="Renk Seç",command=Color).grid(row=2,column=0,sticky=N) # Row 2, Column 0
gui.mainloop()