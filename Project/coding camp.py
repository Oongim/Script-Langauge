# def solution(record):
# #     answer = []
# #     events = []  # [('E','uid1234'),('E','uid4567')]
# #     usersDic = dict()  # {'uid1234':'Prodo', 'uid4567':'Ryun'}
# #
# #     for i in record:
# #         event = i.split()  # ['Enter','uid1234', 'Muzi']
# #         if event[0] == 'Enter':
# #             events.append(('E', event[1]))  # events=[('E','uid1234')]
# #             usersDic[event[1]] = event[2]  # 삽입 usersDIc={'uid1234':'Muzi'}
# #         elif event[0] == 'Leave':  # 이벤트 기록만 하고 usersDic 변경 안한다.
# #             events.append(('L', event[1]))
# #         elif event[0] == 'Change':  # usersDic만 변경
# #             usersDic[event[1]] = event[2]
# #
# #     for i in events:  # [('E','uid1234'),('E','uid4567')]
# #         uid = i[1]
# #         nickname = usersDic[uid]
# #
# #         if i[0] == 'E':
# #             answer.append(nickname + "님이 들어왔습니다.")
# #         elif i[0] == 'L':
# #             answer.append(nickname + "님이 나갔습니다.")
# #
# #     return answer
# #
# #
# # record=["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
# # print(solution(record))

# #중복 되는 경우들을 검사
# def check_Duplication(case_lst,resorted_list,length):
#     check_list = [[] for i in range(length)]
#
#     #체크 리스트에 경우가 되는 키 값들의 값들을 모두 넣어 놓음
#     for listNum in range(length):
#         for i in case_lst:
#             check_list[listNum].append(resorted_list[i][listNum])
#
#     #체크 리스트를 카운트 함수를 이용해서 중복되는 리스트가 있는지 확인해서 리턴
#     for i in range(len(check_list)):
#         if check_list.count(check_list[i])!=1:
#             return False
#     return True
#
# def solution(relation):
#     answer=[]
#     # 후보키 별로 데이터를 모아놓는 리스트
#     resorted_list = [[] for i in range(len(relation[0]))]
#     #조합 될 수 있는 모든 경우의 수를 2진수로 구함
#     AllofCase=[[y for y in range(0,len(relation[0])) if x&(2**y)] for x in range(1,len(relation[0])*len(relation[0]))]
#     #유일성을 갖는 후보키를 저장하는 리스트
#     UniqueMinimality=[]
#
#     #후보키 별로 다시 리스트를 재 구성하는 포문
#     for lst in relation:
#         for i in range(0, len(lst)):
#             resorted_list[i].append(lst[i])
#
#     #모든 경우에서 유일성을 갖는 리스트만 골라냄
#     for caseNum_list in AllofCase:
#         if check_Duplication(caseNum_list,resorted_list,len(relation)):
#             UniqueMinimality.append(caseNum_list)
#     print(UniqueMinimality)
#
#     #UniqueMinimality 리스트를 훑어보는 변하는 변수, 하위 집합일 경우 그대로 아니면 +1
#     cnt=0
#
#     #UniqueMinimality리스트가 안 비어있다면 리스트의 맨 처음 값을 체크 리스트로 넘기고
#     #체크 리스트와 그 다음 리스트를 더한 것을 셋으로 바꾼 후 개수가 그냥 다음 리스트와 수가 같다면 하위 집합이므로 지우고 cnt그대로
#     #아닐시 +1,  하위 집합을 모두 지우면 cnt를 0으로 바꾼후 answer에 추가하고 반복
#     while(UniqueMinimality):
#         checkNum_list=UniqueMinimality.pop(0)
#         while cnt!=len(UniqueMinimality):
#             if len(UniqueMinimality[cnt])==len(set(UniqueMinimality[cnt]+checkNum_list)):
#                 print(UniqueMinimality[cnt])
#                 UniqueMinimality.remove(UniqueMinimality[cnt])
#             else:
#                 cnt+=1
#         cnt=0
#         answer.append(checkNum_list)
#         print()
#         print(answer)
#
#     return len(answer)

def unique(relation,key,Nrow):  #key가 유일성을 만족하는 속성의 집합이라면 True 반환
    for i in range(Nrow-1): #0,1,2,....,Nrow-
        A = []
        for k in key:
            A.append(relation[i][k])
        for j in range(i+1,Nrow):
            B = []
            for k in key:
                B.append(relation[j][k])
            if A==B:
                return False
    return True

def solution(relation):
    Nrow=len(relation)   #relation의 행의 개수
    Ncol=len(relation[0])  #relation의 열의 개수

    superkey=[]
    answer=[]
    #비트를 이용해서 가능한 속성의 집합을 구한다.
    for i in range(1,2**Ncol): #1,2,3...2^Ncol-1
        key=[]
        for j in range(Ncol): #0, 1, 2, ......,Ncol-1, j가 각 속성의 인덱스
            if(i>>j)&1==1: #해당하는 인덱스 속성이 집합에 포함되어야 함
                key.append(j)
        #print(key)
        if unique(relation,key,Nrow):
            superkey.append(key)

    # for x in superkey:
    #     setX=set(x)
    #     flag = True
    #     for y in superkey:
    #         if x != y:
    #             setY=set(y)
    #             if setX.issuperset(setY):
    #                 flag = False
    #                 break
    #     if flag == True:
    #         answer.append(x)


    while(superkey):
        cnt = 0
        checkNum_list=superkey.pop(0)
        while cnt!=len(superkey):
            if len(superkey[cnt])==len(set(superkey[cnt]+checkNum_list)):
                superkey.remove(superkey[cnt])
            else:
                cnt+=1
        answer.append(checkNum_list)


    return len(answer)

print(solution( [["100","ryan","music","2"],
                 ["200","apeach","math","2"],
                 ["300","tube","computer","3"],
                 ["400","con","computer","4"],
                 ["500","muzi","music","3"],
                 ["600","apeach","music","2"]]))