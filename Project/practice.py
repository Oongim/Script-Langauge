
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

number=[]
        mathematics=[]
        i=0
        while i < len(equList):
            if str(0)<=equList[i] <=str(9):
                if  i+1!=len(equList) and str(0)<=equList[i+1] <=str(9):
                    if i+2!=len(equList) and str(0) <= equList[i + 2] <= str(9) or (10*int(equList[i])+int(equList[i+1]))>13:
                        return self.wrong(1)
                    number.append(10*int(equList[i])+int(equList[i+1]))
                    i+=1
                else:
                    number.append(int(equList[i]))

            if equList[i]=="+" or equList[i]=="-" or equList[i]=="*" or equList[i]=="/":
                mathematics.append(equList[i])
            i+=1
        if len(number)>4:
            return self.wrong(1)
        while(mathematics):
            if mathematics.count("*")!=0 or mathematics.count("/")!=0:
                for i in range(len(mathematics)):
                    if mathematics[i]=="*":
                        number[i]=number[i]*number[i+1]
                        number.pop(i+1)
                        mathematics.pop(i)
                        print(number)
                        break
                    elif mathematics[i]=="/":
                        number[i]=number[i]/number[i+1]
                        number.pop(i+1)
                        mathematics.pop(i)
                        print(number)
                        break
            else:
                if mathematics[0] == "+":
                    number[0] = number[0] + number[1]
                    number.pop(1)
                    mathematics.pop(0)
                    print(number)
                    break
                if mathematics[0] == "-":
                    number[0] = number[0] - number[1]
                    number.pop(1)
                    mathematics.pop(0)
                    print(number)
                    break
        print(number)

        print(number, mathematics)
        if number[0]!=24:
            return self.wrong(self.e1.get())
        else:
            return self.right()