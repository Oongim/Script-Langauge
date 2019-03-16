def solution(record):
    answer = []
    events = []  # [('E','uid1234'),('E','uid4567')]
    usersDic = dict()  # {'uid1234':'Prodo', 'uid4567':'Ryun'}

    for i in record:
        event = i.split()  # ['Enter','uid1234', 'Muzi']
        if event[0] == 'Enter':
            events.append(('E', event[1]))  # events=[('E','uid1234')]
            usersDic[event[1]] = event[2]  # 삽입 usersDIc={'uid1234':'Muzi'}
        elif event[0] == 'Leave':  # 이벤트 기록만 하고 usersDic 변경 안한다.
            events.append(('L', event[1]))
        elif event[0] == 'Change':  # usersDic만 변경
            usersDic[event[1]] = event[2]

    for i in events:  # [('E','uid1234'),('E','uid4567')]
        uid = i[1]
        nickname = usersDic[uid]

        if i[0] == 'E':
            answer.append(nickname + "님이 들어왔습니다.")
        elif i[0] == 'L':
            answer.append(nickname + "님이 나갔습니다.")

    return answer


record=["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))