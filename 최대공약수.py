#두 수의 최대 공약수는 두 수를 나누어 떨어지는 가장 큰 수이다. 
#예를 들어 (16, 24)의 최대 공약수는 8이다. 
#두 수를 입력 받아 다음 알고리즘에 의해 최대 공약수를 구하는 프로그램을 작성하라.
#큰 수를 작은 수로 나눈 나머지를 구하라
#큰 수를 작은 수로 대체하고 작은 수는 나머지로 대체하라
#작은 수가 0이 될 때까지 이 과정을 반목하라. 마지막 큰 수가 최대 공약수이다.

print("최대공약수 구하기")
a = int(input("첫번째 수를 입력"))
b = int(input("두번째 수를 입력"))
if a>b:
    while b!=0: 
        c = a%b
        a=b
        b= c
        
    print(f"{a}")
elif b>a:
    while a!=0: 
        c = b%a
        b=a
        a= c    
    print(f"{b}")
# a,b = max(num1,num2),min(num1.num2)
'''while b!=0:
    remainder = a%b
    a,b = b, remainder
result = a  
이렇게도 가능하다'''   

