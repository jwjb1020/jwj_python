#다음과 같은 게임 프로그램을 작성하라.
#플레이어가 처음에 $50을 가지고 있다. 
#동전을 한 번 던져서 앞면(1) 또는 뒷면(2)이 나온다. 
#맞추면 $9을 따고 틀리면 $10을 잃는다. 
#플레이어가 돈을 모두 잃거나 $100이 되면 게임이 종료된다.
#동전을 던져서 나오는 수는 다음 문장을 이용하라.
#from random import randint
#coin = randint(1,2) #1 또는 2를 임의로 발생

from random import randint

money = 50

print("동전게임")
while True:
    start = int(input("1를 눌러 동전을 던지세요,0은 종료"))
    if start ==1:
        coin = randint(1,2)
        if coin ==1:
            money += 9
        elif coin ==2:
            money -=10
    elif start ==0:
        break
    if money< 0:
        print("파산")
        break
    if money>=100:
        
        print(f"\nvictory 너의 돈 :{money} ")
        break         
    print(f"남은돈:{money}")


