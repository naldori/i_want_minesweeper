import tkinter
from tkinter import messagebox
from time import *
import random

#def
blist = []
bblist=[]
bomblist=[0]*71+[1]*10
ifzer=[]
ball=[]
m,n = 0,0

num = 0

def click(lst,num):
    bomb = lst[num][2]
    count = lst[num][5]
    if bomb == 1:
        return ifbomb
    elif count == 0:
        return ifzero
    elif count == 1:
        return ifone
    elif count == 2:
        return iftwo
    elif count == 3:
        return ifthree
    elif count == 4:
        return iffour
    elif count == 5:
        return iffive
    elif count == 6:
        return ifsix
    elif count == 7:
        return ifseven
    elif count == 8:
        return ifeight


def ifbomb():
    photo = tkinter.PhotoImage(file="buttonbomb.png")
    blist[num-1][1].configure(image=photo)
    blist[num-1][1].image=photo
    messagebox.showinfo("게임종료","게임을 다시시작하세요")
    for ba in ball:
        ba.configure(image=photo)
        ba.image=photo

def ifzero():
    photo = tkinter.PhotoImage(file="buttonte.png")
    for ze in ifzer:
        ze.configure(image=photo)
        ze.image=photo
##    blist[num-1][1].configure(image=photo)
##    blist[num-1][1].image=photo

def ifone():
    photo =tkinter.PhotoImage(file="buttonone.png")
    blist[num-1][1].configure(image=photo)
    blist[num-1][1].image=photo

def iftwo():
    photo =tkinter.PhotoImage(file="buttontwo.png")
    blist[num-1][1].configure(image=photo)
    blist[num-1][1].image=photo

def ifthree():
    photo=tkinter.PhotoImage(file="buttonthree.png")
    blist[num-1][1].configure(image=photo)
    blist[num-1][1].image=photo

def iffour():
    photo=tkinter.PhotoImage(file="buttonfour.png")
    blist[num-1][1].configure(image=photo)
    blist[num-1][1].image=photo

def iffive():
    photo=tkinter.PhotoImage(file="buttonfive.png")
    blist[num-1][1].configure(image=photo)
    blist[num-1][1].image=photo

def ifsix():
    photo=tkinter.PhotoImage(file="buttonsix.png")
    blist[num-1][1].configure(image=photo)
    blist[num-1][1].image=photo

def ifseven():
    photo=tkinter.PhotoImage(file="buttonseven.png")
    blist[num-1][1].configure(image=photo)
    blist[num-1][1].image=photo

def ifeight():
    photo=tkinter.PhotoImage(file="buttoneight.png")
    blist[num-1][1].configure(image=photo)
    blist[num-1][1].image=photo





'''
def packing(photo,j):
    globals()["button"+str(j)].configure(image=photo)
    globals()["button"+str(j)].image=photo
'''

#main

random.shuffle(bomblist)
window = tkinter.Tk()
window.geometry("450x450")
window.title("minesweeper")
window.resizable(False,False)


photo = tkinter.PhotoImage(file = "buttonbefore.png")


for j in range(81):

    bblist = []
    bblist.append(j+1)
    bblist.append(0)
    bblist.append(bomblist[j])

    m=(j+1)%9
    n =(j+1)//9
    if m == 0:
        m = 8
        n-=1
    else :
        m-=1
    bblist.append(m)
    bblist.append(n)
    bblist.append(0)
    blist.append(bblist)

for i in range(81):
    if blist[i][2]==1:
        if blist[i][3]==0:
            if blist[i][4]==0:
                blist[i+1][5]+=1
                blist[i+9][5]+=1
                blist[i+10][5]+=1
            elif blist[i][4]==8:
                blist[i-9][5]+=1
                blist[i-8][5]+=1
                blist[i+1][5]+=1
            else:
                blist[i-9][5]+=1
                blist[i-8][5]+=1
                blist[i+1][5]+=1
                blist[i+9][5]+=1
                blist[i+10][5]+=1
                
        elif blist[i][3]==8:
            if blist[i][4]==0:
                blist[i-1][5]+=1
                blist[i+8][5]+=1
                blist[i+9][5]+=1
            elif blist[i][4]==8:
                blist[i-1][5]+=1
                blist[i-10][5]+=1
                blist[i-9][5]+=1
            else:
                blist[i-1][5]+=1
                blist[i-10][5]+=1
                blist[i-9][5]+=1
                blist[i+8][5]+=1
                blist[i+9][5]+=1
        else:
            if blist[i][4]==0:
                blist[i-1][5]+=1
                blist[i+1][5]+=1
                blist[i+8][5]+=1
                blist[i+9][5]+=1
                blist[i+10][5]+=1
            elif blist[i][4]==8:
                blist[i-10][5]+=1
                blist[i-9][5]+=1
                blist[i-8][5]+=1
                blist[i-1][5]+=1
                blist[i+1][5]+=1
            else:
                blist[i-10][5]+=1
                blist[i-9][5]+=1
                blist[i-8][5]+=1
                blist[i-1][5]+=1
                blist[i+1][5]+=1
                blist[i+8][5]+=1
                blist[i+9][5]+=1
                blist[i+10][5]+=1

##for z in range(81):
##    if blist[z][2]==0 and blist[z][5]==0:
##        ifzero.append(z)

for j in range(81):

##    button = tkinter.Button(window, image = photo)
##    button.bind("<Button-1>",clickleft)
    func = click(blist,j)
    globals()["button{}".format(j)] = tkinter.Button(window, image = photo,command = func)
    if blist[j][2]==0 and blist[j][5]==0:
        ifzer.append(globals()["button"+str(j)])
    ball.append(globals()["button"+str(j)])
    blist[j][1]=globals()["button"+str(j)]
    blist[j][1].place(x=blist[j][3]*50,y=blist[j][4]*50)


window.mainloop()




