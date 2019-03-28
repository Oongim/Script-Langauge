def gcd(m,n):
    if m%n==0:
        return n
    return gcd(n,m%n)

x,y=set([int(x) for x in input("두 정수를 입력하세요:").split()])
print(gcd(x,y))