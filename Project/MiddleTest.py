# def Slump(*strs):
#     result=[]
#
#     for str in  strs:
#             if str[0]=="D" or str[0]=="E":
#                 fcnt = 0
#                 for i in range(1,len(str)):
#                     if str[i]=="G" and fcnt and i==len(str)-1:
#                         result.append("YES")
#                         break
#                     elif i==len(str)-1 and not str[i]=="G":
#                         result.append("NO")
#                         break
#                     elif str[i]=="D" or str[i]=="E":
#                         if fcnt:
#                             fcnt = 0
#                         else:
#                             result.append("NO")
#                             break
#                     elif str[i]=="F":
#                         fcnt+=1
#                     else:
#                         result.append("NO")
#                         break
#             else:
#                 result.append("NO")
#     return result
#
# print(Slump("DFFFFG"))

# def reverse(number):
#     number=str(number)
#     r_num=''
#     for i in range(len(number)-1,0-1,-1):
#         r_num+=number[i]
#     return int(r_num)
# N,K=input("단의 수와 항의 수 입력:").split()
#
# N=int(N)
# K=int(K)
# numList=[0]*(K+1)
# for i in range(K+1):
#     numList[i]=str(N*i)
#     numList[i]=reverse(numList[i])
#
# print(max(numList))

# N=eval(input("수 입력:"))
# sum=0
# for i in range(1,N):
#     sum+=N*i+i
#
# print(sum)

# #10-35
# from tkinter import *
#
# class Ball:
#     def __init__(self):
#         self.x  = 10
#         self.y  = 10
#         self.dx = 2
#         self.dy = 2
#
# class BallAnimate:
#     def animate(self):
#         while self.isRunning:
#             self.canvas.after(self.timeSleep)
#             self.canvas.update()
#             self.canvas.delete("ball")
#             for ball in self.ballList:
#                 if ball.x >=self.width-5 or ball.x<=0:
#                     ball.dx *=-1
#                 if ball.y >=self.height-5 or ball.y<=0:
#                     ball.dy *=-1
#                 ball.x+=ball.dx
#                 ball.y+=ball.dy
#                 self.canvas.create_oval(ball.x-3,ball.y-3,ball.x+3,ball.y+3,fill="red",tags="ball")
#     def stop(self):
#         self.isRunning=False
#     def resume(self):
#         self.isRunning=True
#         self.animate()
#     def add(self):
#         self.ballList.append(Ball())
#     def sub(self):
#         self.ballList.pop()
#     def faster(self):
#         self.timeSleep-=20
#     def slower(self):
#         self.timeSleep += 20
#     def __init__(self):
#         window=Tk()
#         window.title("공 튀기기")
#         self.width = 500
#         self.height=300
#         self.canvas = Canvas(window,bg="white",width=self.width,height=self.height)
#         self.canvas.pack()
#         self.ballList=[]
#         self.timeSleep=100
#         self.isRunning=True
#         frame=Frame(window)
#         frame.pack()
#         Button(frame,text="정지",command=self.stop).pack(side=LEFT)
#         Button(frame,text="재시작",command=self.resume).pack(side=LEFT)
#         Button(frame,text="+",command=self.add).pack(side=LEFT)
#         Button(frame,text="-",command=self.sub).pack(side=LEFT)
#         Button(frame,text="빠르게",command=self.faster).pack(side=LEFT)
#         Button(frame,text="느리게",command=self.slower).pack(side=LEFT)
#         self.animate()
#         window.mainloop()
#
# BallAnimate()

# dice=[int(x) for x in input("수 입력:").split()]
# check3=False
# check2=False
# for i in range(1,6+1):
#     if dice.count(i)==3:
#         check3=True
#     elif dice.count(i)==2:
#         check2=True
#     elif dice.count(i)==5:
#         check3 = True
#         check2 = True
#
# if check3 and check2:
#     print("YES")
# else:
#     print("NO")
#
# import random
# class Card:
#     suitNames=['클럽','다이아몬드','하트','스페이드']
#     rankNames=['에이스','2','3','4','5','6','7','8','9','10','잭','퀸','킹']
#
#     def __init__(self,suit,rank):
#         self.suit =suit
#         self.rank=rank
#
#     def __str__(self):
#         return Card.suitNames[self.suit],Card.rankNames[self.rank]
# class Deck:
#     def __init__(self):
#         self.deck=random.sample([x for x in range(0, 51)], 5)
#         self.print()
#     def print(self):
#         for i in range(5):
#             print(i+1,"번째 카드: "+Card(self.deck[i]//13,self.deck[i]%13).__str__()[0],Card(self.deck[i]//13,self.deck[i]%13).__str__()[1])
#
# Deck()