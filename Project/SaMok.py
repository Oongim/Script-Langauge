from tkinter import *
import random

class TicTacToe:
    def again(self):
        for i in range(6*7):
            self.buttonList[i]["image"]=self.imageList[2]
            self.buttonList[i]["text"]=' '

    def click(self,Col):
        for r in range(5,-1,-1):
            if self.buttonList[r*7+Col]["text"]==' ':
                self.buttonList[r*7+Col].configure(image=self.imageList[self.turn])
                self.buttonList[r * 7 + Col].configure(text=self.turn)
                self.turn= not self.turn
                break


    def __init__(self):
        self.turn=False
        window=Tk()
        self.imageList=[]
        self.imageList.append(PhotoImage(file="image/o.gif"))
        self.imageList.append(PhotoImage(file="image/x.gif"))
        self.imageList.append(PhotoImage(file="image/empty.gif"))
        self.buttonList=[]
        frame1=Frame(window)
        frame1.pack()
        for r in range(6):
            for c in range(7):
                self.buttonList.append(Button(frame1,text=' ',image=self.imageList[2],command=lambda Col=c:self.click(Col)))
                self.buttonList[r*7+c].grid(row=r,column=c)
        frame2=Frame(window)
        frame2.pack()
        Button(frame2, text="다시 생성",command=self.again).pack()
        window.mainloop()

TicTacToe()