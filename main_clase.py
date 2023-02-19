import tkinter
from tkinter import messagebox
import random

#정의

bomblist = [1]*10+[0]*71

blist = []
bblist=[]
ifzer=[]
ball=[]
m,n = 0,0

class buttons(tkinter.Button):
    image = ""
    command=None
    num =0
    def __init__(self,*args,**kwargs):
        tkinter.Button.__init__(self,*args,**kwargs)

    def num(self,x):
        self.num = x
    def ifclick(self,lst):
        bomb = lst[self.num][2]
        count = lst[self.num][5]
        if bomb == 1:
            return buttons.ifbomb(self)
        elif count == 0:
            return buttons.ifzero(self)
        elif count == 1:
            return buttons.ifone(self)
        elif count == 2:
            return buttons.iftwo(self)
        elif count == 3:
            return buttons.ifthree(self)
        elif count == 4:
            return buttons.iffour(self)
        elif count == 5:
            return buttons.iffive(self)
        elif count == 6:
            return buttons.ifsix(self)
        elif count == 7:
            return buttons.ifseven(self)
        elif count == 8:
            return buttons.ifeight(self)
    def ifbomb(self):
        global ball
        photo = tkinter.PhotoImage(file="buttonbomb.png")
        self.configure(image=photo)
        self.image=photo
##        messagebox.showinfo("게임종료","게임을 다시시작하세요")
##        for ba in ball:
##            ba.configure(image=photo)
##            ba.image=photo

    def ifzero(self):
        photo = tkinter.PhotoImage(file="buttonte.png")
        for ze in ifzer:
            ze.configure(image=photo)
            ze.image=photo
    ##    blist[num-1][1].configure(image=photo)
    ##    blist[num-1][1].image=photo

    def ifone(self):
        photo =tkinter.PhotoImage(file="buttonone.png")
        self.configure(image=photo)
        self.image=photo

    def iftwo(self):
        photo =tkinter.PhotoImage(file="buttontwo.png")
        self.configure(image=photo)
        self.image=photo

    def ifthree(self):
        photo=tkinter.PhotoImage(file="buttonthree.png")
        self.configure(image=photo)
        self.image=photo

    def iffour(self):
        photo=tkinter.PhotoImage(file="buttonfour.png")
        self.configure(image=photo)
        self.image=photo

    def iffive(self):
        photo=tkinter.PhotoImage(file="buttonfive.png")
        self.configure(image=photo)
        self.image=photo

    def ifsix(self):
        photo=tkinter.PhotoImage(file="buttonsix.png")
        self.configure(image=photo)
        self.image=photo

    def ifseven(self):
        photo=tkinter.PhotoImage(file="buttonseven.png")
        self.configure(image=photo)
        self.image=photo

    def ifeight(self):
        photo=tkinter.PhotoImage(file="buttoneight.png")
        self.configure(image=photo)
        self.image=photo

#메인

random.shuffle(bomblist)
win = tkinter.Tk()
win.geometry("450x450")
win.title("minesweeper")
win.resizable(False,False)

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

for x  in range(81):
    
    b = buttons(win,image=photo)
    b.num(x)
    c=b.ifclick(blist)

    b.command=c
    if blist[x][2]==0 and blist[x][5]==0:
        ifzer.append(b)
    ball.append(b)
    blist[x][1]=b
    b.place(x=blist[x][3]*50,y=blist[x][4]*50)

win.mainloop()

'''

'''
