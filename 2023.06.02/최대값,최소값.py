#사용자로부터 5개의 정수형 숫자를 입력받아, 
#입력받은 숫자들 중에서 최댓값과 최솟값을 찾고, 이를 출력하는 프로그램을 작성하세요.
#입력받은 숫자는 1 이상 100 이하의 자연수입니다.
#입력받은 숫자 중 중복된 숫자가 있을 수 있습니다.

maxNum = 0
minNum = 100

for i in range(5):
    num = int(input(f"{i+1}번째 숫자  입력해주세요"))
    if num > maxNum:
        maxNum = num
    if num < minNum:
        minNum = num
output = f"최대값:{maxNum}, 최소값:{minNum}"
print(output)     
