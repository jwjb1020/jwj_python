def numPo(n):
    sum = 0
    for num in str(n):
        sum+=int(num)
    return sum    
        
n=input("숫자를 입력해주세요")   
print(numPo(n))

