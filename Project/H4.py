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
#         print("폭: {0},높이: {1}, 넓이: {2}, 둘레: {3}".format(self.width,self.height,self.getArea(),self.getPerimeter()))
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
#
#     def getName(self):
#         return self.__name
#     def getSymbol(self):
#         return self.__symbol
#     def getPreviousClosingPrice(self):
#         return self.__previousClosingPrice
#     def setPreviousClosingPrice(self,price):
#         self.__previousClosingPrice=price
#
#     def getCurrentPrice(self):
#         return self.__currentPrice
#     def setCurrentPrice(self,price):
#         self.__currentPrice=price
#
#     def printChangePriceRate(self):
#         print("가격 변화율은 {0:.2f}%".format((-self.__previousClosingPrice+self.__currentPrice)/self.__previousClosingPrice*100))
# uml=Stock("INTC","Intel Corporation",20500,20350)
#
# print("Symbol",uml.getSymbol())
# print("Name",uml.getName())
# print("PreviousClosingPrice",uml.getPreviousClosingPrice())
# print("CurrentPrice",uml.getCurrentPrice())
#
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


