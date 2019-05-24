# # 7.1
# class Rectangle:
#     def __init__(self,x=1,y=2):
#         self.width=x
#         self.height=y
#
#     def getArea(self):
#         return self.width*self.height
#     def getPerimeter(self):
#         return 2*self.width+2*self.height
#
#     def printInform(self):
#         print("폭: {0},높이: {1}, 넓이: {2:.2f}, 둘레: {3}".format(self.width,self.height,self.getArea(),self.getPerimeter()))
#
#
# rec1,rec2=Rectangle(4,10),Rectangle(3.5,35.7)
#
# rec1.printInform()
# rec2.printInform()


# # 7.2
#
# class Stock:
#     def __init__(self,symbol,name,previousClosingPrice,currentPrice):
#         self.__symbol=symbol
#         self.__name=name
#         self.__previousClosingPrice=previousClosingPrice
#         self.__currentPrice=currentPrice
#     def getName(self):
#         return self.__name
#     def getSymbol(self):
#         return self.__symbol
#     def getPreviousClosingPrice(self):
#         return self.__previousClosingPrice
#     def setPreviousClosingPrice(self,price):
#         self.__previousClosingPrice=price
#     def getCurrentPrice(self):
#         return self.__currentPrice
#     def setCurrentPrice(self,price):
#         self.__currentPrice=price
#     def printChangePriceRate(self):
#         print("가격 변화율은 {0:.2f}%".format((-self.__previousClosingPrice+self.__currentPrice)/self.__previousClosingPrice*100))
# uml=Stock("INTC","Intel Corporation",20500,20350)
# print("Symbol",uml.getSymbol())
# print("Name",uml.getName())
# print("PreviousClosingPrice",uml.getPreviousClosingPrice())
# print("CurrentPrice",uml.getCurrentPrice())
# uml.printChangePriceRate()


# #7.4
# SLOW,MEDIUM,FAST=range(3)
# class Fan:
#     def __init__(self,speed=SLOW,on=False,radius=5,color="BLUE"):
#         self.__speed=speed
#         self.__on=on
#         self.__radius=radius
#         self.__color=color
#
#     def getSpeed(self):
#         return self.__speed
#     def getOn(self):
#         if self.__on==True:
#             return "On"
#         else:
#             return "OFF"
#     def getRadius(self):
#         return self.__radius
#     def getColor(self):
#         return self.__color
#
#     def setSpeed(self,speed):
#         self.__speed=speed
#     def setOn(self,on):
#         self.__on=on
#     def setRadius(self,radius):
#         self.__radius=radius
#     def setColor(self,color):
#         self.__color=color
#
#     def PrintInfo(self):
#         print("속도는 {0}, 크기는 {1}, 색상은 {2}, 전원 {3}".format(self.__speed,self.__radius,self.__color,self.getOn()))
#
# fan1=Fan(FAST,True,10,"YELLOW")
# fan2=Fan(MEDIUM)
# fan1.PrintInfo()
# fan2.PrintInfo()

# #7-8
# import time
#
# class StopWatch:
#     def __int__(self):
#         self.startTime=time.time()
#         self.endTime=0
#     def start(self):
#         self.startTime=time.time()
#     def stop(self):
#         self.endTime=time.time()
#     def getElapsedTime(self):
#         print("경과 시간은: ",(self.endTime-self.startTime)*1000,"ms")
#
# sum=0
# S=StopWatch()
# S.start()
# for i in range(1000000):
#     sum +=i
# S.stop()
# S.getElapsedTime()

# #12-1
# class GeometircObject:
#     def __init__(self,color,isfill):
#         self.color=color
#         self.isfill=bool(isfill)
#     def getColor(self):
#         return self.color
#     def getIsfill(self):
#         return self.isfill
# class Triangle(GeometircObject):
#     def printInfo(self):
#         print("넓이 :{0:.2f}, 둘레 :{1}, 색상 :{2}, 색상채움여부 :{3}".format(
#             self.getArea(),self.getPerimeter(),self.getColor(),self.getIsfill()))
#     def __init__(self,side1=1.0,side2=1.0,side3=1.0,color="BLUE",isfill=False):
#         self.side1=side1
#         self.side2=side2
#         self.side3=side3
#         GeometircObject.__init__(self,color,isfill)
#
#         self.printInfo()
#
#     def getSide1(self):
#         return self.side1
#     def getSide2(self):
#         return self.side2
#     def getSide3(self):
#         return self.side3
#
#     def getArea(self):
#         s=(self.side1+self.side2+self.side3)/2
#         return (s*(s-self.side1)*(s-self.side2)*(s-self.side3))**0.5
#     def getPerimeter(self):
#         return self.side1+self.side2+self.side3
#
#     def __str__(self):
#         return "Triangle: side1 = "+str(self.side1)+"side2 = "+str(self.side2) + "side3 = "+str(self.side3)
# side1,side2,side3,color,isfill=input("세 변의 길이와 색, 색채움 여부 입력:").split()
# tri=Triangle(int(side1),int(side2),int(side3),color,int(isfill))

# #13-1
# f= open("test.txt","w")
# f.write("morning kpu game morning\n morning entertaiment\n morning")
# f.close()
#
# filename=input("파일 이름 입력:")
# f=open(filename)
# s=input("제거할 단어:")
# content=f.read()
# f.close()
# f=open(filename,"w")
# f.write(content.replace(s,""))

# #13-2
#
# f=open(input("파일이름을 입력하세요:"),'r')
#
# c=f.read()
# print("문자 ",len(c),"개")
# w=c.split()
# print("단어 ",len(w),"개")
# e=c.split("\n")
# print("행 ",len(e),"개")
# f.close()


# # 14-4
# from tkinter import *
# from tkinter.filedialog import askopenfilename
# def fileopen():
#     global filename
#     #filename=e1.get()
#     filename=askopenfilename()
# def handle():
#     global filename
#     f=open(filename)
#     content=f.read()
#     histogram=[0]*26
#     new=content.lower()
#     for  c in new:
#         if c.isalpha():
#             histogram[ord(c)-97]+=1
#     text.delete(1.0,END)
#     for i in range(26):
#         text.insert(END,chr(i+97) +" -"+str(histogram[i]).rjust(3)+"번 나타납니다.\n")
#     f.close()
#
# window=Tk()
# frame1=Frame(window)
# frame1.pack()
#
# scrollbar=Scrollbar(frame1)
# scrollbar.pack(side=RIGHT,fill=Y)
# text=Text(frame1,width=40,height=10,wrap=WORD,yscrollcommand=scrollbar.set)
# text.pack()
# scrollbar.config(command=text.yview)
# frame2=Frame(window)
# frame2.pack()
# Label(frame2,text="파일명을 입력하세요:").pack(side=LEFT)
# e1=Entry(frame2,width=20,text="")
# e1.pack(side=LEFT)
# Button(frame2,text="열기",command=fileopen).pack(side=LEFT)
# Button(frame2,text="결과 보기",command=handle).pack(side=LEFT)
#
# window.mainloop()

#
# #14-7
# from tkinter import *
#
# def display(histogram):
#     canvas.delete("grim")
#     # 빈도수 최대값을 구한다.
#     maxCount = int(max(histogram))
#     canvas.create_line(10, height - 10, width - 10, height - 10, tags="grim")
#     barW = (width - 20) / 26
#     for i in range(26):
#         canvas.create_rectangle(i * barW + 10, height - (height - 25) * histogram[i] / maxCount-11,
#                                      (i + 1) * barW + 10, height - 10, tags="grim")
#         canvas.create_text(i * barW + 10 + 10, height - 10 + 5, text=chr(i + ord('a')), tags="grim")
#         canvas.create_text(i * barW + 10 + 10, height - (height - 25) * histogram[i] / maxCount - 16,
#                                 text=histogram[i], tags="grim")
# def handle():
#     filename = e1.get()
#     f=open(filename)
#     content=f.read()
#     histogram=[0]*26
#     new=content.lower()
#     for  c in new:
#         if c.isalpha():
#             histogram[ord(c)-97]+=1
#     display(histogram)
#     f.close()
#
# window=Tk()
# frame1=Frame(window)
# frame1.pack()
#
# width=500
# height=300
# canvas=Canvas(window,width=width,height=height,bg="white")
# canvas.pack()
# frame2=Frame(window)
# frame2.pack()
# Label(frame2,text="파일명을 입력하세요:").pack(side=LEFT)
# e1=Entry(frame2,width=30,text="")
# e1.pack(side=LEFT)
# Button(frame2,text="결과 보기",command=handle).pack(side=LEFT)
#
# window.mainloop()








