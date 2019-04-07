
def solution(food_times, k):

    timelist=[]
    for i in range(len(food_times)):
        timelist.append([food_times[i],i])

    timelist.sort()
    print(timelist)

    while k>=len(timelist)*timelist[0][0]:
        cnt = 0
        print("enter",k,len(timelist))
        if len(timelist)==0:
            return -1
        else:
            temp=timelist[0][0]
        print(timelist)
        print(temp, "k=", k)
        k-=len(timelist)*temp
        while cnt<len(timelist):

            timelist[cnt][0]-=temp
            if timelist[cnt][0]==0:
                print(timelist[cnt])
                timelist.remove(timelist[cnt])
            else:
                cnt+=1
        if len(timelist)==0:
            return -1
    print(k)
    timelist.sort(key=lambda k:k[1])
    print(timelist)
    return timelist[k%len(timelist)][1]+1


print(solution([8, 3, 3,5,3],30))