#사용자로부터 두 개의 정수와 연산자를 입력받아, 
#입력된 연산자에 따라 두 수의 사칙연산 결과를 출력하는 계산기 프로그램을 작성하세요.
#프로그램은 사용자가 "exit"을 입력할 때까지 계속해서 작동합니다.
#입력받은 숫자는 어떠한 값이든 상관없습니다.
#입력받은 연산자는 +, -, *, / 중 하나입니다.
#나눗셈 연산 결과는 실수형으로 출력하세요.
#분모가 0일 경우, "0으로 나눌 수 없습니다."를 출력하세요.
#사용자가 "exit"을 입력할 경우, 프로그램을 종료하세요.

while True:
    a = input("[간단한계산기]\n\n 첫번째수를 입력하세요(exit 입력시 종료):")
    if a == "exit":
        break
    b = input("두번째 수 입력")
    op= input("연산자 입력 ( +,-,*,/)")

    a = int(a)
    b = int(b)

    if op =="+":
        result = a+b
        output = f"{a} + {b} = {result}"
    elif op == "-":
        result = a-b
        output = f"{a} - {b} = {result}" 
    elif op == "*":
        result = a-b
        output = f"{a} * {b} = {result}"       
    elif op == "/":
        if b == 0:
            output = "0으로 나눌 수 없어요"
        else:
            result = a/b
            output = f"{a} / {b} = {result}"
    else:
        output="잘못된 연산자"
    print(output)        
