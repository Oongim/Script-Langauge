
def getArea(x1,y1,x2,y2,x3,y3):
    s1=((x2-x1)**2+(y2-y1)**2)**0.5
    s2=((x3-x1)**2+(y3-y1)**2)**0.5
    s3=((x3-x2)**2+(y3-y2)**2)**0.5
    s=(s1+s2+s3)/2
    area=(s*(s-s1)*(s-s2)*(s-s3))**0.5
    return area


x1,y1,x2,y2,x3,y3=eval(input("세 꼭지점:"))
print(getArea(x1,y1,x2,y2,x3,y3))