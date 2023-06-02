#두 주사위를 던졌을 때, 합이 7이 되면 이김, 그렇지 않으면 지는 간단한 주사위 게임을 만들어보세요.

import random

       
        

while True:
    start = int(input("주사위를 던질려면 1을 입력하세요.그만하려면 0을 입력하세용"))        
    if start ==1:
        a = random.randint(1,6)
        b = random.randint(1,6)
        sum = a+b
        if sum == 7:
            print(f"{a},{b}")
            print("correct")
            break
        else:
            print(f"{a},{b}")
            print("restart?")
            continue
    elif start ==0:
        break
