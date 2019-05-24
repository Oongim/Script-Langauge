def solution(m, musicinfos):
    answer = ''
    musicinfo = []
    for infos in range(len(musicinfos)):
        musicinfo.append(infos.split())
    return musicinfo

print(solution( "ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"] ) )