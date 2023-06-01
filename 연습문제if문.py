#사용자로부터 cm 단위의 길이를 입력 받는다. 
#입력 값이 음수이면 "잘못 입력하였습니다"라는 메시지를 출력하고 
#양수이면 길이를 인치로 변환하여 출력하는 프로그램을 작성하라. 
#1인치 = 2.54cm

data = int(input("길이(cm)를 입력해주세요."))
if data < 0: 
    print("잘못 입력하였습니다.")
else :
    inch=data * 0.393701
    print(f"{inch}인치")

#사용자로부터 이수한 학점을 입력 받는다. 
# 학점이 40학점 미만이면 "1학년입니다"를 출력하고, 
# 40이상 80미만이면 "2학년입니다"를 출력한다. 
# 학점이 80이상이면 "졸업반입니다"를 출력하는 프로그램을 작성하라.

score=int(input("이수한 학점을 입력"))
if score < 40:
    print("1학년")
elif score >= 40:
    if score >=80:
        print("졸업반")
    else : 
        print("2학년") 

#사용자로부터 현재 시간을 나타내는 1~12의 숫자를 입력 받는다. 
# 또 "am" 혹은 "pm"을 입력 받고 경과 시간을 나타내는 값을 입력 받는다. 
# 이로부터 최종 시간이 몇 시인지 출력하는 프로그램을 작성하라.
nowHour = int(input("현재시간을 입력해주세요."))
AmPm=input("오전이면 am, 오후면 pm을 입력해주세요")
ahead=int(input("몇시간이 경과했나요?"))

newHour = (nowHour+ahead)%12
if newHour == 0:
    newHour=12

if(nowHour+ahead)//12%2==1:
    if AmPm =="am":
        AmPm = "pm"
    else:
        AmPm = "am"
print(f"최종시간:{newHour}{AmPm}")        
        