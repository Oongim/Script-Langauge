pound=eval(input("몸무게를 파운드로 입력하세요:"))
inch=eval(input("키를 인치로 입력하세요:"))

weight=pound*0.45359237
tall=inch*0.0254
print("BMI는 ", weight/(tall*tall),"입니다." )