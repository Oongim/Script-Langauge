'''
class Node:
    def __init__(self,num,coordinate):
        self.coordinate=coordinate
        self.num=num
        self.left=None
        self.right=None
    def getNum(self):
        return self.num

class Level: #같은 레벨에 들어있는 모든 노드들을 갖는다.
    def __init__(self,level):#노드의 y값이 level
        self.level=level
        self.nodes=[] #해당 레벨에 들어있는 Node 객체들

def makeTree(nodes,start,end,level,parent):
    if level >= len(nodes):
        #print("out")
        return
    else:
        for node in nodes[level].nodes:
            print(level, "start:", start, "end:", end, "left", parent.coordinate[0] - 1, node.coordinate[0], end)
            if start<=node.coordinate[0]<=parent.coordinate[0]-1:
                print(parent.coordinate, "LEFT", node.coordinate)
                parent.left=node
                makeTree(nodes, start, node.coordinate[0]-1, level+1, node)
                makeTree(nodes, node.coordinate[0] + 1, end, level + 1, node)

            print(level,"start:",start,"end:",end,"right", parent.coordinate[0] + 1, node.coordinate[0], end)
            if parent.coordinate[0]+1<=node.coordinate[0]<=end:
                print(parent.coordinate,"right",node.coordinate)
                parent.right=node
                makeTree(nodes, start, node.coordinate[0] - 1, level + 1, node)
                makeTree(nodes, node.coordinate[0]+1, end, level + 1, node)

def preorder(node,list):
    if node:
        list.append(node.num)
        preorder(node.left,list)
        preorder(node.right,list)

def postorder(node,list):
    if node:
        postorder(node.left,list)
        postorder(node.right,list)
        list.append(node.num)
def solution(nodeinfo):
    level=[]
    for i in range(len(nodeinfo)):
        flag=True
        for l in level:
            if l.level == nodeinfo[i][1]:
                l.nodes.append(Node(i+1,nodeinfo[i]))
                flag=False
                break
        if flag==True:
            l=Level(nodeinfo[i][1])
            l.nodes.append(Node(i+1,nodeinfo[i]))
            level.append(l)
    level.sort(key=lambda l:l.level,reverse=True)
    for l in level:
        l.nodes.sort(key=lambda X:X.coordinate[0])
    root = level[0].nodes[0]

    makeTree(level, 0, root.coordinate[0] - 1, 1, root)
    makeTree(level, root.coordinate[0] + 1, 100001,1, root)

    preorderList=[]
    preorder(root,preorderList)
    postorderList=[]
    postorder(root, postorderList)
    return [preorderList,postorderList]

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))
'''


# def solution(word, pages):
#     word=word.lower()
#     #기본점수, 외부링크수, 외부링크들, 홈페이지
#     scanning=[]
#     for page in pages:
#         page=page.lower()
#         page=page.split()
#         #print(page)
#         # 홈페이지 찾기
#         j = 0
#         while True:
#             if page[j].find("content=") != -1:
#                 break
#             j += 1
#             start=page[j].find("\"")
#             end=page[j].find("\"",start+1)
#         homepage = page[j][start+1:end]
#
#         #외부링크 찾기, 기본 점수
#         j+=1
#         while True:
#             if page[j].find("<body>") != -1:
#                 break
#             j += 1
#         j += 1
#         basicScore=0
#         outlinks=[]
#         while page[j].find("</body>")==-1:  #끝까지 검색
#
#
#             if page[j].find("href=")!=-1:
#                 start = page[j].find("\"")
#                 end = page[j].find("\"", start + 1)
#                 outlinks.append(page[j][start+1:end])
#
#             copy=page[j]
#             for c in page[j]:
#                 if not c.isalpha():
#                     copy=copy.replace(c,' ')
#             #알파벳이 아닌 것은 전부 공란으로 바꾸고 split
#             copy=copy.split()
#             for w in copy:
#                 if w == word:
#                     basicScore += 1
#             j+=1
#         print("홈페이지=",homepage,"외부링크=",outlinks,"기본점수=",basicScore)
#
#         scanning.append([basicScore,homepage,outlinks])
#     result = []
#     for i in range(len(scanning)):
#         matchingScore=scanning[i][0]  #기본점수를 더한다
#         #나를 링크하는 다른 홈페이지들을 찾아서 링크점수들을 더한다.
#         for  j in range(len(scanning)):
#             if i !=j and scanning[i][1] in scanning[j][2]:
#                 matchingScore+=scanning[j][0]/scanning[j][2].count(scanning[i][1])
#         result.append(matchingScore)
#     largest=0
#     print(result)
#     for i in range(1,len(result)):
#         if result[largest]<result[i]:
#             largest=i
#
#     return largest
#
#
#
#
# print(solution("blind",["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n <meta charset=\"utf-8\">\n <meta property=\"og:url\" content=\"https://a.com\"/>\n</head> \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n <meta charset=\"utf-8\">\n <meta property=\"og:url\" content=\"https://b.com\"/>\n</head> \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n <meta charset=\"utf-8\">\n <meta property=\"og:url\" content=\"https://c.com\"/>\n</head> \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))
#
# def check(board,N,i,j):
#     if j>N-2 or i >N-2: #컬럼은 N-2 보다 작아야 함
#         return False
#     true_case=[[(1,0),(1,1),(1,2)],[(1,0),(2,0),(2,-1)],[(1,0),(2,0),(2,1)],[(1,0),(1,-1),(1,-2)],[(1,-1),(1,0),(1,1)]]
#     isPass=1
#     for num in range(5):
#         for case in true_case[num]:
#             if  i+case[0]<N and j+case[1] <N and board[i+case[0]][j+case[1]]==board[i][j]:
#                 isPass = num+1
#             else:
#                 isPass=0
#                 break
#         if isPass:
#             break
#     if isPass: return isPass
#     else: return False
# def remove(board,n,i,j):
#     if n==0:
#         return False
#     b_b = [[(0, 1), (0, 2)], [(0, -1), (1, -1)], [(0, +1), (1, +1)], [(0, -1), (0, -2)], [(0, -1), (0, 1)]]
#     isPass = True
#     for case in b_b[n]:
#         if board[i+case[0]][j+case[1]]==0:
#             isPass = True
#         else:
#             isPass=False
#             break
#
#     if isPass: return True
#     else: return False
#
# def solution(board):
#     answer = 0
#     N=len(board)
#     for i in range(N-1):
#         for j in range(N-1):
#             if board[i][j] and remove(board,check(board,N,i,j),i,j):
#                 n=board[i][j]
#                 print(n)
#                 for k in range(N):
#                     if board[k].count(n):
#                         board[k].remove(n)
#
#
#     return board
#
# print(solution([[0,0,0,0,0,0,0,0,0,0],
#                 [0,0,0,0,0,0,0,0,0,0],
#                 [0,0,0,0,0,0,0,0,0,0],
#                 [0,0,0,0,0,0,0,0,0,0],
#                 [0,0,0,0,0,0,4,0,0,0],
#                 [0,0,0,0,0,4,4,0,0,0],
#                 [0,0,0,0,3,0,4,0,0,0],
#                 [0,0,0,2,3,0,0,0,5,5],
#                 [1,2,2,2,3,3,0,0,0,5],
#                 [1,1,1,0,0,0,0,0,0,5]]))



# def systemSum(num,n):
#     DIGITS="0123456789ABCDEF"
#     if num==0:
#         return "0"
#     result=""
#     while num:
#         remainder = num%n
#         result=DIGITS[remainder]+result
#         num=num//n
#     return result
# def solution(n, t, m, p):
#     answer = ''
#     systemList=""
#     cnt=0
#     while len(systemList)<=p + m * t:
#         systemList+=systemSum(cnt,n)
#         cnt+=1
#
#     for i in range(t):
#         answer+=systemList[(p-1) + i*m]
#     print(systemList)
#     return answer
#
# print(solution(2,4,2,1))




# def solution(msg):
#     wordList=[]
#     answer = []
#
#     for i in range(26):
#         wordList.append(chr(ord("A")+i))
#
#     while len(msg):
#         for i in range(len(msg)):
#             if wordList.count(msg[:len(msg)-i]):
#                 wordList.append(msg[:len(msg)-i]+msg[-i])
#                 answer.append(wordList.index(msg[:len(msg)-i])+1)
#                 msg=msg[len(msg)-i:]
#                 break
#
#     return answer
#
# print(solution("TOBEORNOTTOBEORTOBEORNOT"))

# def solution(files):
#     answer = []
#
#     parsingList=[]
#     index=0
#     for file in files:
#         i=0
#         head=""
#         num=""
#         while not file[i].isnumeric():
#             head+=file[i]
#             i+=1
#
#         while i < len(file) and file[i].isnumeric():
#             num+=file[i]
#             i+=1
#         parsingList.append([head.lower(),int(num),index])
#         index+=1
#     parsingList.sort()
#     for i in range(len(parsingList)):
#         answer.append(files[parsingList[i][2]])
#     return answer
#
# print(solution(["foo9.txt", "foo010bar020.zip", "F-15", "B-14 Tomcat"]))

def change(items):
    str=''
    for i in range(len(items)):
        if i + 1 < len(items) and items[i + 1] is '#':
            str += items[i].lower()
        elif items[i] is '#':
            pass
        else:
            str += items[i]
    return str

def solution(m, musicinfos):
    answer = ['',0]
    musicinfo = []
    for item in musicinfos:
        musicinfo.append(item.split(sep=','))

    for item in musicinfo:
        time1=item[0].split(sep=':')
        time2 = item[1].split(sep=':')
        rtime1=int(time2[0])-int(time1[0])
        rtime2=int(time2[1]) - int(time1[1])
        playtime=rtime1*60+rtime2

        melody2=change(item[3])

        melody=''
        for i in range(playtime):
            melody+=melody2[i%len(melody2)]
        mel=change(melody)

        m_s=change(m)
        if m_s in mel:
            if answer[1] < playtime:
                answer=[item[2],playtime]

    if answer[0] is '':
        answer[0] ='(None)'
    return answer[0]

# print(solution( "CC", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B",
#                                     "05:52,08:08,BAR%#,CC#BCC#BCC#BCC#BCC#BCC#BCC#B",
#                                     "05:52,08:20,BARsd%#,CC#BCC#BCC#BCC#BCC#BCC#BCC#B",
#                                      ] ) )
#print(solution("C#D#E#F#G#G",["12:03,12:55,HELLO,GC#D#E#F#G#","12:03,12:12,eeeEELLO,CC#D#E#F#G#G"]))
print(solution("C#D",["12:03,12:07,HELLO,DC#C#C#","12:03,12:12,eeeEELLO,BCDE"]))
#print(solution("EB",["12:03,12:07,HELLO,BCDE","12:03,12:12,eeeEELLO,BCDE"]))
'''
def change(data):
    n = 0
    new_data = ''
    save = ''
    sharp_check = False
    if(len(data) == 1):
        return data
    while(True):
        save = data[n]
        if(data[n+1] == '#'):
            data.replace('#','',1)
            save = data[n].lower()
            new_data += save
            sharp_check = True
        if sharp_check == False:
            new_data += save
        else:
            n += 1
            if(len(data) == n+1):
                break
            else:
                sharp_check = False
        n +=1
        if (len(data) == n + 1):
            break
    if(sharp_check == False):
        new_data += data[n]
    return new_data

def solution(m, musicinfos):

    for i in range(len(musicinfos)):
        musicinfos[i] = musicinfos[i].split(",")       # ","로 스플릿
        playtime = (int(musicinfos[i][1][0:2]) + int(musicinfos[i][1][3:])) - (int(musicinfos[i][0][0:2]) + int(musicinfos[i][0][3:]))
        musicinfos[i].append(playtime)
        musicinfos[i][3] = change(musicinfos[i][3])

    m = change(m)
    print(m)
    print(musicinfos)
    answer = []
    for data in musicinfos:

        if(len(data[3]) > data[4]):
            data[3] = data[3][0:data[4]]
        elif (len(data[3]) == data[4]):
            pass
        else:
            data[3] = data[3] * (data[4] // len(data[3])) + data[3][0:data[4]%len(data[3])]
            print(data)
        if m in data[3]:
            if (len(answer) == 0):
                answer.append(data)
            elif(answer[0][4] < data[4]):
                answer[0] = data

    if (len(answer) == 0):
        return '(None)'
    elif (len(answer) == 1):
        return answer[0][2]

print(solution("C#D#E#F#G#G",["12:03,12:55,HELLO,GC#D#E#F#G#","12:03,12:12,eeeEELLO,CC#D#E#F#G#G"]))
#print(solution("C#D",["12:03,12:07,HELLO,DC#C#C#","12:03,12:12,eeeEELLO,BCDE"]))
#print(solution("EB",["12:03,12:07,HELLO,BCDE","12:03,12:12,eeeEELLO,BCDE"]))
'''