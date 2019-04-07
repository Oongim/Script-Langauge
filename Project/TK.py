# #9-1
# from tkinter import *
# def up():
#     global y
#     if y!=0:
#         y=y-5
#
#     canvas.delete("ball")
#     canvas.create_oval(x, y, x+10, y+10, fill="red", tags="ball")
# def down():
#     global y
#     if y != 195:
#         y = y + 5
#     canvas.delete("ball")
#     canvas.create_oval(x, y, x + 10, y + 10, fill="red", tags="ball")
# def left():
#     global x
#     if x != 0:
#         x = x - 5
#     canvas.delete("ball")
#     canvas.create_oval(x, y, x + 10, y + 10, fill="red", tags="ball")
# def right():
#     global x
#     if x != 300:
#         x = x + 5
#     canvas.delete("ball")
#     canvas.create_oval(x, y, x + 10, y + 10, fill="red", tags="ball")
# window=Tk()
# x=10
# y=10
# canvas=Canvas(window,width=300,height=200,bg='white')
# canvas.pack()
# canvas.create_oval(10,10,20,20,fill="red",tags="ball")
# frame=Frame(window)    #따로 프레임 만들어서 상관없이 만들 수 있다
# frame.pack()
#
# Button(frame,text="상",command=up).pack(side=LEFT)
# Button(frame,text="하",command=down).pack(side=LEFT)
# Button(frame,text="좌",command=left).pack(side=LEFT)
# Button(frame,text="우",command=right).pack(side=LEFT)
#
# window.mainloop()

##################꿀팁for루프#######################################
# from tkinter import *
# window=Tk()
# frame=Frame(window
# for i in range(4):
#     Button(frame,text=str(i),command=lambda index=i:common(index)).pack(side=LEFT)
#
# window.mainloop()
##############################################################
# #9-2
# from tkinter import *
# window=Tk()
# def calculate():
#     money=eval(e1.get())
#     year=eval(e2.get())
#     interest=eval(e3.get())
#     futureValue=money*((1+interest/100)**(year*12))
#     print( futureValue)
#     l5.configure(text="{0:.2f}".format(futureValue))
#
# Label(window,text="투자금").grid(row=0,column=0,sticky='W')
# Label(window,text="기간").grid(row=1,column=0,sticky='W')
# Label(window,text="월이율").grid(row=2,column=0,sticky='W')
# Label(window,text="미래 가치").grid(row=3,column=0,sticky='W')
# l5=Label(window,text="")
# l5.grid(row=3,column=1,sticky='E')
#
# e1=Entry(window,justify=RIGHT)
# e1.grid(row=0,column=1)
# e2=Entry(window,justify=RIGHT)
# e2.grid(row=1,column=1)
# e3=Entry(window,justify=RIGHT)
# e3.grid(row=2,column=1)
#
# b1=Button(window,text="계산하기",command=calculate).grid(row=4,column=1,sticky="E")
# window.mainloop()

'''
#9-3
from tkinter import *

class Radio:
    def display(self):
        self.canvas.delete("grim")
        if self.v.get()==1: #직사각형
            if self.f.get()==1: #채우기
                self.canvas.create_rectangle(10, 10, 290, 190, tag="grim",fill='red')
            else:
                self.canvas.create_rectangle(10, 10, 290, 190, tag="grim")
        else:
            if self.f.get() == 1:  # 채우기
                self.canvas.create_oval(10, 10, 290, 190, tag="grim",fill='red')
            else:
                self.canvas.create_oval(10, 10, 290, 190, tag="grim")
    def __init__(self):
        window=Tk()
        window.title("라디오 버튼")
        self.canvas=Canvas(window,bg="white",width=300,height=200)
        self.canvas.create_rectangle(10,10,290,190,tag="grim")
        self.canvas.pack()
        frame=Frame(window)
        frame.pack()
        self.v=IntVar()# 정수 클래스의 객체로 만든다  self.v.get()
        Radiobutton(frame,text="직사각형",variable=self.v,value=1,command=self.display).pack(side=LEFT)
        Radiobutton(frame,text="타원",variable=self.v,value=2,command=self.display).pack(side=LEFT)
        self.f=IntVar()
        Checkbutton(frame,text="채우기",variable=self.f,command=self.display).pack(side=LEFT)

        window.mainloop()

Radio()
'''
'''
#10.33
from tkinter import *
import random
class Histogram:
    def display(self):
        self.canvas.delete("grim")
        histogram=[0]*26
        for i in range(1000):
            histogram[random.randint(0,25)]+=1
        #빈도수 최대값을 구한다.
        maxCount=int(max(histogram))
        self.canvas.create_line(10,self.height-10,self.width-10,self.height-10,tags="grim")
        barW=(self.width-20)/26
        for i in range(26):
            self.canvas.create_rectangle(i*barW+10,self.height-(self.height-20)*histogram[i]/maxCount,
                                        (i+1)*barW+10,self.height-10,tags="grim")
            self.canvas.create_text(i*barW+10+10,self.height-10+5,text=chr(i+ord('a')),tags="grim")
            self.canvas.create_text(i * barW + 10 + 10,self.height-(self.height-20)*histogram[i]/maxCount-5, text=histogram[i], tags="grim")
    def __init__(self):
        window = Tk()
        window.title("빈도수")
        self.width=500
        self.height=300
        self.canvas=Canvas(window,width=self.width,height=self.height,bg="white")
        self.canvas.pack()
        Button(window,text="히스토그램 그리기",command=self.display).pack()
        window.mainloop()
Histogram()
'''
'''
#10-35
from tkinter import *

class Ball:
    def __init__(self):
        self.x  = 5
        self.y  = 5
        self.dx = 2
        self.dy = 2

class BallAnimate:
    def animate(self):
        while self.isRunning:
            self.canvas.after(self.timeSleep)
            self.canvas.update()
            self.canvas.delete("ball")
            for ball in self.ballList:
                if ball.x >=self.width-5 or ball.x<=0:
                    ball.dx *=-1
                if ball.y >=self.height-5 or ball.y<=0:
                    ball.dy *=-1
                ball.x+=ball.dx
                ball.y+=ball.dy
                self.canvas.create_oval(ball.x-3,ball.y-3,ball.x+3,ball.y+3,fill="red",tags="ball")
    def stop(self):
        self.isRunning=False
    def resume(self):
        self.isRunning=True
        self.animate()
    def add(self):
        self.ballList.append(Ball())
    def sub(self):
        self.ballList.pop()
    def faster(self):
        self.timeSleep-=10
    def slower(self):
        self.timeSleep += 10
    def __init__(self):
        window=Tk()
        window.title("공 튀기기")
        self.width = 500
        self.height=400
        self.canvas = Canvas(window,bg="white",width=self.width,height=self.height)
        self.canvas.pack()
        self.ballList=[]
        self.timeSleep=100
        self.isRunning=True
        frame=Frame(window)
        frame.pack()
        Button(frame,text="정지",command=self.stop).pack(side=LEFT)
        Button(frame,text="재시작",command=self.resume).pack(side=LEFT)
        Button(frame,text="+",command=self.add).pack(side=LEFT)
        Button(frame,text="-",command=self.sub).pack(side=LEFT)
        Button(frame,text="빠르게",command=self.faster).pack(side=LEFT)
        Button(frame,text="느리게",command=self.slower).pack(side=LEFT)
        self.animate()
        window.mainloop()

BallAnimate()
'''
'''
from tkinter import *
import random
class LinearSearch:
    def endTextBox(self):
        window = Tk()
        window.title("끝났습니다.")
        Label(window, text="찾았습니다").pack()
        self.selected=-1
    def animate(self):
        self.canvas.delete("grim")
        for i in range(20):
            if(self.selected==i):
                self.canvas.create_rectangle(i * (self.width - 10) / 20 + 5,
                                             (20 - self.sampleNumList[i]) * (self.height - 10) / 20 + 10,
                                             (i + 1) * (self.width - 10) / 20 + 5, self.height,fill='black',tag="grim")
                if eval(self.e1.get())==self.sampleNumList[i]:
                    self.endTextBox()
            else:
                self.canvas.create_rectangle(i*(self.width-10)/20+5,(20-self.sampleNumList[i])*(self.height-10)/20+10,
                                         (i+1)*(self.width-10)/20+5,self.height,tag="grim")
            self.canvas.create_text(i*(self.width-10)/20+(self.width-10)/20/2+5,(20-self.sampleNumList[i])*(self.height-10)/20-(self.height-10)/20/2+10
                                    ,text=(self.sampleNumList[i]), tags="grim")
    def next(self):
        self.selected+=1
        self.animate()
    def reset(self):
        self.sampleNumList = random.sample([x for x in range(1, 21)], 20)
        self.animate()
    def __init__(self):
        window=Tk()
        window.title("선형 검색 애니메이션")
        self.width=600
        self.height=200
        self.canvas=Canvas(window,bg="white",width=self.width,height=self.height)
        self.canvas.pack()
        self.sampleNumList=random.sample([x for x in range(1,21)],20)
        self.selected=-1
        frame=Frame(window)
        frame.pack()
        Label(frame,text="키를 입력하세요:").pack(side=LEFT)
        self.e1=Entry(frame,width=5,justify=RIGHT)
        self.e1.pack(side=LEFT)
        Button(frame,text="다음단계",command=self.next).pack(side=LEFT)
        Button(frame,text="재설정",command=self.reset).pack(side=LEFT)
        self.animate()
        window.mainloop()

LinearSearch()
'''
'''
from tkinter import *
import random
class SelectSort:
    def animate(self):
        self.canvas.delete("grim")
        for i in range(20):
            if(self.selected==i):
                self.canvas.create_rectangle(i * (self.width - 10) / 20 + 5,
                                             (20 - self.sampleNumList[i]) * (self.height - 10) / 20 + 10,
                                             (i + 1) * (self.width - 10) / 20 + 5, self.height,fill='black',tag="grim")
            else:
                self.canvas.create_rectangle(i*(self.width-10)/20+5,(20-self.sampleNumList[i])*(self.height-10)/20+10,
                                         (i+1)*(self.width-10)/20+5,self.height,tag="grim")
            self.canvas.create_text(i*(self.width-10)/20+(self.width-10)/20/2+5,(20-self.sampleNumList[i])*(self.height-10)/20-(self.height-10)/20/2+10
                                    ,text=(self.sampleNumList[i]), tags="grim")
    def next(self):
        self.selected=(self.selected+1)%20
        temp=self.sampleNumList[self.selected]
        for i in range(self.selected,20):
            if(self.selected+1==self.sampleNumList[i]):
                self.sampleNumList[self.selected]=self.selected+1
                self.sampleNumList[i]=temp
        self.animate()
    def reset(self):
        self.selected=-1
        self.sampleNumList = random.sample([x for x in range(1, 21)], 20)
        self.animate()
    def __init__(self):
        window=Tk()
        window.title("선택 정렬 애니메이션")
        self.width=600
        self.height=200
        self.canvas=Canvas(window,bg="white",width=self.width,height=self.height)
        self.canvas.pack()
        self.sampleNumList=random.sample([x for x in range(1,21)],20)
        self.selected=-1
        frame=Frame(window)
        frame.pack()
        Button(frame,text="다음단계",command=self.next).pack(side=LEFT)
        Button(frame,text="재설정",command=self.reset).pack(side=LEFT)
        self.animate()
        window.mainloop()
SelectSort()
'''

from tkinter import *
from PIL import Image, ImageTk
import random
class CardGame:
    def animate(self):
        pass

    def reset(self):
        self.card = random.sample([x for x in range(1, 52)], 4)
        self.img = [ImageTk.PhotoImage(Image.open("card.png").crop((self.cwidth * ((self.card[i]) % 13),
                                                                    self.cheight * ((self.card[i]) // 13),
                                                                    self.cwidth * ((self.card[i]) % 13 + 1),
                                                                    self.cheight * ((self.card[i]) // 13 + 1)
                                                                    ))) for i in range(4)]
        self.L1.configure(image=self.img[0])
        self.L1.image=self.img[0]
        self.L2.configure(image=self.img[1])
        self.L2.image = self.img[1]
        self.L3.configure(image=self.img[2])
        self.L3.image = self.img[2]
        self.L4.configure(image=self.img[3])
        self.L4.image = self.img[3]

    def enter(self):
        self.e1.get()
    def __init__(self):
        window=Tk()
        window.title("24점 게임")
        self.card = random.sample([x for x in range(1, 52)], 4)
        self.cwidth=1343/13
        self.cheight=577/4

        Button(window, text="새로고침", command=self.reset).pack()
        self.frame1=Frame(window)
        self.frame1.pack()
        self.img=[ImageTk.PhotoImage(Image.open("card.png").crop((self.cwidth*((self.card[i])%13),
                                                                 self.cheight*((self.card[i])//13),
                                                                 self.cwidth*((self.card[i])%13+1),
                                                                 self.cheight*((self.card[i])//13+1)
                                                                ))) for i in range(4)]
        self.L1=Label(self.frame1, image=self.img[0])
        self.L1.pack(side=LEFT)
        self.L2 = Label(self.frame1, image=self.img[1])
        self.L2.pack(side=LEFT)
        self.L3 = Label(self.frame1, image=self.img[2])
        self.L3.pack(side=LEFT)
        self.L4 = Label(self.frame1, image=self.img[3])
        self.L4.pack(side=LEFT)
        frame2=Frame(window)
        frame2.pack()
        Label(frame2, text="수식을 입력하세요:").pack(side=LEFT)
        self.e1 = Entry(frame2)
        self.e1.pack(side=LEFT)
        Button(frame2,text="확인",command=self.enter).pack(side=LEFT)

        self.animate()
        window.mainloop()
CardGame()
