money=eval(input("약정 금액을 입력하세요:"))

profit=eval(input("연이율을 입력"))

t=eval(input("약정 기갼(년)을 입력하세요:"))

print("월 납입금은 ",money/(1+profit/1200)**(t*12),"입니다")