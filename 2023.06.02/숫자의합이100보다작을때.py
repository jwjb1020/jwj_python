#사용자로부터 정수형 숫자를 입력받아, 
#입력받은 숫자들의 합이 100보다 작을 때까지 숫자를 계속 입력받고, 
#입력받은 숫자들의 합을 출력하는 프로그램을 작성하세요.
#입력받은 숫자는 1 이상 100 이하의 자연수입니다
sum=0
while sum < 100:
    n = int(input("숫자를 입력하세요"))
    sum += n
output = f"입력받은 숫자들의 합 : {sum}"
print(output)