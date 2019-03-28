def getRightmostLowestPoint(points):
    global largest_num
    largest_num=0

    if abs(max(points)) >=abs(min(points)):
        largest_num=abs(max(points))
    else:
        largest_num = abs(min(points))

    max_num=0
    max_RightDownPoint = []
    for i in range(0,len(points),2) :
        d=((points[i]-(-largest_num))**2 + (points[i+1]-(largest_num))**2)
        if max_num< d:
            max_num=d
            max_RightDownPoint=points[i],points[i+1]
    return max_RightDownPoint

List=[float(x) for x in input("6개의 점을 입력하세요: ").split()]

print(getRightmostLowestPoint(List))

# # 3-6
# n= eval(input("아스키 코드 입력:"))
# print("아스키 코드 {0}의 문자는 {1}".format(n,chr(n)))
