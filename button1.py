import tkinter
from tkinter import messagebox
from time import *

##num = 0
##
##def Func():
##    messagebox.showinfo("end", "you died")
##
##def clickNotBomb():
##    global num
##    photo = tkinter.PhotoImage(file = "buttonone.png")
##    button1.configure(image = photo)
##    button1.image = photo
##    
##    
##
###main
##window = tkinter.Tk()
##window.geometry("700x700")
##
##photo = tkinter.PhotoImage(file = "buttonbefore.png")
##button1 = tkinter.Button(window, image = photo, command = clickNotBomb)
##button2 = tkinter.Button(window, image = photo, command = clickNotBomb)
##
##button1.place(x =0,y= 0)
##button2.place(x =100,y= 100)
##
##
##window.mainloop()


def clickNotBomb():
    global num
    photo = tkinter.PhotoImage(file = "buttonone.png")
    button1.configure(image = photo)
    button1.image = photo
    
    

#main
window = tkinter.Tk()
window.geometry("700x700")
button = []

photo = tkinter.PhotoImage(file = "buttonbefore.png")
button1 = tkinter.Button(window, image = photo, command = clickNotBomb)
button2 = tkinter.Button(window, image = photo, command = clickNotBomb)
button.append(button1)
button.append(button2)



button[0].place(x =0,y= 0)
button[1].place(x =100,y= 100)


window.mainloop()
