##minesweeper
from tkinter import *
from tkinter import messagebox
from time import *
import random

class buttonsobj:
    
    file = "buttonbefore.png"
    bombcount = 0
    x=0
    y=0
    buttonbutton = []
    
    def __init__(self,lst,buttonlistnum,bombornot = 0):
        self.x = (buttonlistnum+1)%9
        self.y = (buttonlistnum+1)//9+1
        if lst[buttonlistnum] != None:
            bombornot = 1
    def bombcount(self):
        bombcount = self.bombcount
        self.bombcount = bombcount
    def ifyouclick(self):
        if self.bombcount ==0:
            photo = PhotoImage(file = self.file)
            button.configure(image = photo)
            button.image = photo
    def bombbutton(self,tkwin):
        button = Button(tkwin,image = self.buttongraphic, command = ifyouclick)
        buttonsobj.buttonbutton.append(button)

def buttonplace():
    shortname = buttonsobj.buttonbutton
    for b in shortname:
        num = shortname.index(b)
        m = (num+1)%9
        n = (num+1)//9+1
        b.place(x = m, y =n)
        
            
    #폭탄 개수 세는 함수 올자리
       

#메인 부분
if __name__ == "__main__":
    buttons = [None]*71
    judgebomb = [] #폭탄개수 판별할때 쓸거임
    buttonclass=[]

    for i in range(10):
        buttons.append(1)

    random.shuffle(buttons) #여기까지하면 폭탄 무작위 배치 완료


    print(buttons)


    window = Tk()
    window.geometry("450x450")

    for j in range(81):
        button = buttonsobj(buttons,j)
        buttonclass.append(button)

    
    buttonplace()
    


    window.mainloop()

