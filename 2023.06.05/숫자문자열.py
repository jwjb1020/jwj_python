#숫자를 문자열로 변화하는 방법은 str(num)을 이용한다. 
#str(12)  '12'가 된다. 반대로 문자열을 숫자로 변환하려면 
#int(string)을 이용한다. int('12')  12가 된다. 
#이를 이용하여 1부터 1000까지의 숫자의 각 자리수의 합을 모두 구하라. 
#예를 들어 234  2+3+4=9가 된다
#[Hint] sum = 0 for s in '234':    sum += int(s)

total = 0
for num in range(1,1001):
    digital_sum = 0
    for digit in str(num):
        digital_sum+= int(digit)
    total+=digital_sum
print(total)        