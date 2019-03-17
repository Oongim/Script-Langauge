import math

def GCdistance(x1,y1,x2,y2):
    d=6371.01*math.acos(math.sin(x1)*math.sin(x2)+math.cos(x1)*math.cos(x2)*math.cos(y1-y2))
    return d

x1,y1=eval(input("첫번째 점을 60분법 각으로 입력하세요"))
x2,y2=eval(input("두번째 점을 60분법 각으로 입력하세요"))

x1=math.radians(x1)
y1=math.radians(y1)
x2=math.radians(x2)
y2=math.radians(y2)
print(GCdistance(x1,y1,x2,y2))