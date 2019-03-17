Set=eval(input("1과 100사이의 정수를 입력하세요: "))
List=list(Set)
List.sort()

while(List):
    print(List[0]," - ",List.count(List[0]),"번 나타납니다.")
    cnt=List.count(List[0])
    while(cnt):
        List.pop(0)
        cnt-=1