temper=eval(input("화씨 -58F 와 -41F 사이의 온도를 입력하세요: "))
wind=eval(input("풍속을 시간 당 마일 단위로 입력하세요: "))

Twc=35.74+0.6215*temper-35.75*(wind**0.16)+0.4275*temper*(wind**0.16)
print("체감온도는 ",Twc,"입니다")