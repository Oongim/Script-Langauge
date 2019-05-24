from tkinter import *
import random

class TicTacToe:
    def check(self,Row,Col):
        if Row==0:
            if self.tokenList[Row][Col] == self.tokenList[Row +1][Col] and self.tokenList[Row][Col] == self.tokenList[Row + 2][Col]:
                return True
        elif Row==1:
            if self.tokenList[Row][Col] == self.tokenList[Row -1][Col] and self.tokenList[Row][Col] == self.tokenList[Row + 1][Col]:
                return True
        elif Row==2:
            if self.tokenList[Row][Col] == self.tokenList[Row -1][Col] and self.tokenList[Row][Col] == self.tokenList[Row - 2][Col]:
                return True
        if Col==0:
            if self.tokenList[Row][Col] == self.tokenList[Row][Col+1] and self.tokenList[Row][Col] == self.tokenList[Row][Col+2]:
                return True
        elif Col==1:
            if self.tokenList[Row][Col] == self.tokenList[Row][Col-1] and self.tokenList[Row][Col] == self.tokenList[Row][Col+1]:
                return True
        elif Col==2:
            if self.tokenList[Row][Col] == self.tokenList[Row][Col-1] and self.tokenList[Row][Col] == self.tokenList[Row][Col-2]:
                return True
        if Row==0 and Col==0:
            if self.tokenList[Row][Col] == self.tokenList[Row+1][Col+1] and self.tokenList[Row][Col] == self.tokenList[Row+2][Col+2]:
                return True
        elif Row ==  1 and Col == 1:
            if self.tokenList[Row][Col] == self.tokenList[Row + 1][Col + 1] and self.tokenList[Row][Col] == self.tokenList[Row -1][Col -1]:
                return True
        elif Row == 2 and Col == 2:
            if self.tokenList[Row][Col] == self.tokenList[Row - 1][Col - 1] and self.tokenList[Row][Col] == self.tokenList[Row - 2][Col - 2]:
                return True
        if Row==0 and Col==2:
            if self.tokenList[Row][Col] == self.tokenList[1][1] and self.tokenList[Row][Col] == self.tokenList[2][0]:
                return True
        elif Row ==  1 and Col == 1:
            if self.tokenList[Row][Col] == self.tokenList[0][2] and self.tokenList[Row][Col] == self.tokenList[2][0]:
                return True
        elif Row == 2 and Col == 0:
            if self.tokenList[Row][Col] == self.tokenList[0][2] and self.tokenList[Row][Col] == self.tokenList[1][1]:
                return True
        else:
            return False
    def again(self):
        for i in range(9):
            self.labelList[i]["image"]=self.imageList[2]
            self.tokenList[i//3][i%3]=2
    def click(self,Row,Col):
        if self.tokenList[Row][Col]==2:
            self.count+=1
            labelText=["X 차례", "O 차례"]
            self.labelList[Row*3+Col]["image"]=self.imageList[self.turn]
            self.tokenList[Row][Col]=self.turn

            if self.check(Row,Col):
                self.count = 0
                window = Tk()
                if self.turn:
                    Label(window,text="X의 승리").pack()
                else:
                    Label(window, text="O의 승리").pack()
                Button(window, text="재실행", command=self.again).pack()
                window.mainloop()

            elif self.count==9:
                self.count = 0
                window = Tk()
                Label(window, text="비겼습니다.").pack()
                Button(window,text="재실행",command=self.again).pack()

                window.mainloop()

            self.label.configure(text=labelText[self.turn])
            self.turn = not self.turn

    def __init__(self):
        self.turn=False
        window=Tk()
        self.imageList=[]
        self.imageList.append(PhotoImage(file="image/o.gif"))
        self.imageList.append(PhotoImage(file="image/x.gif"))
        self.imageList.append(PhotoImage(file="image/empty.gif"))
        self.labelList=[]
        self.tokenList=[[2 for i in range(3)] for j in range(3)]
        self.count=0
        frame1=Frame(window)
        frame1.pack()
        for r in range(3):
            for c in range(3):
                self.labelList.append(Button(frame1,image=self.imageList[2],command=lambda Row=r,Col=c:self.click(Row,Col)))
                self.labelList[r*3+c].grid(row=r,column=c)
        frame2=Frame(window)
        frame2.pack()
        self.label=Label(frame2, text="O 차례")
        self.label.pack()
        window.mainloop()

TicTacToe()