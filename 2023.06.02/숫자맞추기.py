#숫자 맞추기 게임 프로그램
#1~100 사이의 난수를 만들고 사용자가 1~100 사이의 수를 입력하여 맞추는 프로그램. 5회까지 맞추지 못하면 종료
#힌트 주기
import random
i=0
chance = 5
answer = random.randint(1, 100)
while i < 5:
    a = int(input("숫자를 입력해주세요"))
    if(answer == a ):
        print("정답")
        break
    else:
        if answer>a:
            print("up")
        elif answer<a:
            print("down")
               
    i+=1
    chance-=1
    print(f"남은기회:{chance}번")
print("종료")        
