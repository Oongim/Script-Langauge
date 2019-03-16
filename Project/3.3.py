import math

def getArea(s1,s2,s3):
    s=(s1+s2+s3)/2
    area=(s*(s-s1)*(s-s2)*(s-s3))**0.5
    return area

def GCdistance(x1,y1,x2,y2):
    x1 = math.radians(x1)
    y1 = math.radians(y1)
    x2 = math.radians(x2)
    y2 = math.radians(y2)
    d=6371.01*math.acos(math.sin(x1)*math.sin(x2)+math.cos(x1)*math.cos(x2)*math.cos(y1-y2))
    return d

x1,y1=35.1768201,126.7735892  #광주
x2,y2=35.1645701,129.0015892 #부산
x3,y3=37.7637326,128.8824475 #강원+강릉
x4,y4=37.565289,126.8491259 #서울특별시


area1=getArea(GCdistance(x1,y1,x2,y2),GCdistance(x2,y2,x3,y3),GCdistance(x3,y3,x1,y1))
area2=getArea(GCdistance(x1,y1,x3,y3),GCdistance(x1,y1,x4,y4),GCdistance(x3,y3,x4,y4))

print("네 도시의 추정 넓이: ",area1+area2)