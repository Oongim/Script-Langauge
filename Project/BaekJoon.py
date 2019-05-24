'''
testlength=eval(input())
string=[]
for i in range(testlength):
    string.append([int(x) for x in input().split()])

for test in string:
    if test[2]%test[0]==0:
        answer=test[0]*100
        answer += test[2] // test[0]
    else:
        answer = (test[2]%test[0])*100
        answer += test[2] // test[0] + 1

    print(answer)
'''

# testlength=eval(input())
# result=[0]*testlength
# string=[]
# for i in range(testlength):
#     string.append([ eval(input()),[x for x in input()],[x for x in input()] ])
# #  string=[ 5 , [WBBWW] , [WBWBW]
#
# for case in string:
#     cnt=0
#     if case[1].count("W")>case[2].count("W"):
#                 cnt+=case[1].count("W")-case[2].count("W")
#     else:
#         cnt += case[2].count("W") - case[1].count("W")
#     #print("Ddd",cnt)
#     check=0
#     for i in range(case[0]):
#         if case[1][i] != case[2][i]:
#             check+=1
#     cnt+=(check-cnt)//2
#     print(cnt)
# 4
# 5
# WBBWW
# WBWBW
# 7
# BBBBBBB
# BWBWBWB
# 4
# WWBB
# BBWB
# 13
# WBWBWWWWBBWBW
# BWWWBBBWWWBBW



testlength=eval(input())
result=[]
for i in range(testlength):
    list=[x for x in input().split()]
    num=eval(list[0]+list[1]+list[2])==int(list[4])
    if num==True:
        result.append("correct")
    else:
        result.append("wrong answer")

for num in result:
    print(num)