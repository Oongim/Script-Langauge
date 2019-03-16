present=312032486
birth=60*60*24*365*5//7
death=60*60*24*365*5//13
migration=60*60*24*365*5//45

for i in [1,2,3,4,5]:
    print(i*5,"년후 인구: ",present+((birth-death+migration)*i))