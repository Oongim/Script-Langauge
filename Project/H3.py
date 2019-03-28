# #4-1
# while(True):
#     a,b,c=eval(input("a,b,c,를 입력하세여: "))
#
#     if type((b**2-4*a*c)**0.5)==complex:
#         print("실근은 없습니다")
#     elif (b**2-4*a*c)**0.5>0:
#         r = (b ** 2 - 4 * a * c) ** 0.5
#         print("실근은",(-b+r)/2*a,"과",(-b-r)/2*a,"입니다.")
#     elif (b**2-4*a*c)**0.5==0:
#         print("실근은",-b/2*a," 입니다.")

#
#
# #4-24
# import random
#
# while(True):
#     form=random.choice(("크로바","다이아몬드","하트","스페이드"))
#     number=random.choice(("A","2","3","4","5","6","7","8","9","10","J","Q","K"))
#     print("당신이 뽑은 카드는 "+form+" "+number+"입니다.")


# #4-27
# def PointInTriangle(pos):
#     if pos[0]>=0 and pos[1] >=0 and 100-0.5*pos[0] >= pos[1] :
#         print("점은 삼각형의 내부에 있습니다.")
#     else:
#         print("점은 삼각형의 내부에 있지 않습니다.")
# while(True):
#     list=[float(x) for x in input("점의 x와 y 좌표값을 입력하세요:").split()]
#     list=tuple(list)
#     PointInTriangle(list)

#5.39
print("매출액: {0:.2f}".format((25000000-(5000000*0.08+5000000*0.1))/0.12+10000000))


# #5.42
# import random
#
# def check_position(x,y):
#     if x<0:
#         print("1번")
#         return 1
#     elif y<0:
#         print("4번")
#         return 4
#     elif 100-x >= y:
#         print("3번")
#         return 3
#     else:
#         print("2번")
#         return 2
# rate=[]
# while(len(rate)!=1000):
#     x,y=random.randint(-100,100),random.randint(-100,100)
#     rate.append(check_position(x,y))
# print("홀수 영역에 꽃힐 가능성 :",(rate.count(1)+rate.count(3))/len(rate)*100,"%")

# #6.3
# def reverse(number):
#     number=str(number)
#     r_num=''
#     for i in range(len(number)-1,0-1,-1):
#         r_num+=number[i]
#     return int(r_num)
#
# def isPalindrome(number):
#     r_num=reverse(number)
#
#     if(r_num==number):
#         return True
#     return False
# while True:
#     num=eval(input("정수를 입력하세요:"))
#     print(reverse(num))
#
#     print(isPalindrome(num))

# #6-4
# def reverse(number):
#     number=str(number)
#     r_num=''
#     for i in range(len(number)-1,0-1,-1):
#         r_num+=number[i]
#     print(int(r_num))
#
# num=eval(input("정수를 입력하세요:"))
# reverse(num)

# #6-5
# def displaySortedNumbers(num1,num2,num3):
#     print("정렬된 숫자는",num1,num2,num3,"입니다.")
#
#
# n1,n2,n3=set([float(x) for x in input("세 개의 수를 입력하세요:").split()])
#
# displaySortedNumbers(n1,n2,n3)

# #6-12
# def printChars(ch1,ch2,numberPerLine):
#     count=0
#     for i in range(ord(ch1),ord(ch2)+1):
#         print(chr(i),end=' ')
#         if (count+1)%numberPerLine==0:
#           print()
#         count+=1
#
# printChars('1','Z',10)

# #6-13
# sum=0
# print("i     m(i)")
# for i in range(1,20+1):
#     sum+=i/(i+1)
#     print("{0}     {1}".format(i,sum))

# #15-18
# global count
# count=0
# def hanoi(ndisks, startPeg=1, endPeg=3):
#     global count
#     if ndisks:
#         hanoi(ndisks-1, startPeg, 6-startPeg-endPeg)
#         count += 1
#         print(startPeg, "번 기둥의",  ndisks, "번 원반을", endPeg, "번 기둥에 옮깁니다.",count,"번 옮겼습니다.")
#         hanoi(ndisks-1, 6-startPeg-endPeg, endPeg)
# n=eval(input("디스크의 개수를 입력하세요:"))
#
# print("옮기는 순서는 다음과 같습니다.")
#
# hanoi(n)

# #15-19
#
# def decimalToBinary(value):
#     if value==0:
#         return ""
#
#     return decimalToBinary(value//2)+str(value%2)
#
# num=eval(input("10진수를 입력하세요:"))
# print(decimalToBinary(num))
################################################################
#15-20

# def decimalToHex(value):
#     if value==0:
#         return ""
#     r= value%16
#     if r==15:
#         s='F'
#     elif r==14:
#         s='E'
#     elif r==13:
#         s='D'
#     elif r == 12:
#         s = 'C'
#     elif r == 11:
#         s = 'B'
#     elif r == 10:
#         s = 'A'
#     else:
#         s=str(r)
#
#     return decimalToHex(value//16)+s
#
# num=eval(input("10진수를 입력하세요:"))
# print(decimalToHex(num))
###########################################################
