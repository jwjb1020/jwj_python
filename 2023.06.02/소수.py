#임의의 자연수 n이 입력되면 2부터 n까지의 모든 소수를 출력하는 프로그램. 
#소수는 1과 자기자신으로만 나누어 떨어지는 수, 예 5, 7

n = int(input("자연수를 입력"))
for i in range(2,n+1):
    flag =1
    for j in range(2,i):
        if i%j == 0:
            flag = 0
    if flag == 1:
        print(i, end=" ")
    else:
        flag= 1    