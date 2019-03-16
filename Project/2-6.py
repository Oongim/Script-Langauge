n= eval(input("0과 1000사이 숫자 입력:"))

sum=0
r=0
while n>0:
    r=r*10+n%10
    n=n//10

print(r)