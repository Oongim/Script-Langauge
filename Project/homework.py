def sumColumn(m,columnIndex):
    global Sum
    Sum=0
    for i in columnIndex:
        Sum+=i[m]
    return Sum

list1=[float(i) for i in input("3x4 행렬의 행 0 번에 대한 원소를 입력하세요: ").split()]
list2=[float(i) for i in input("3x4 행렬의 행 1 번에 대한 원소를 입력하세요: ").split()]
list3=[float(i) for i in input("3x4 행렬의 행 2 번에 대한 원소를 입력하세요: ").split()]
columnIndex=[list1,list2,list3]

for i in range(0,len(columnIndex)+1):
    print("열 ",i,"번 원소의 총 합은 ",sumColumn(i,columnIndex))
