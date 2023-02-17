from tkinter import *
from tkinter import simpledialog,messagebox

gui = Tk()
screen_width = gui.winfo_screenwidth()
screen_height = gui.winfo_screenheight()

x_cordinate = int((screen_width/2) - (450/2))
y_cordinate = int((screen_height/2) - (450/2))

gui.geometry("{}x{}+{}+{}".format(450, 450, x_cordinate, y_cordinate))
gui.title("Palindrom")

s1 = StringVar()
def Palindrom():
    global s1
    reversed_s1 = "".join(reversed(s1.get()))
    if(str(s1.get()) == str(reversed_s1)):
        messagebox.showinfo("Bilgi",f"Bu yazı bir palindrom yazı\nGirilen değer : {s1.get()} | Ters çevirilmiş değer : {reversed_s1}")
    else:
        messagebox.showerror("Bilgi",f"Bu yazı bir palindrom yazı değil.\nGirilen değer : {s1.get()} | Ters çevirilmiş değer : {reversed_s1}")

Label(gui,text="Bir yazı giriniz : ").grid(row=0,column=0,sticky=W)
Entry(gui,text="Bir yazı giriniz : ",textvariable=s1).grid(row=0,column=1,sticky=W)
Button(gui,text="Palindrom Kontrol",command=Palindrom).grid(row=1,column=0,sticky=N)

gui.mainloop()