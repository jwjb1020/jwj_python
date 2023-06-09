def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
table = {"1":sum, "2":sub, "3":mul, "4":div}
op = input("연산 입력(1,2,3,4)")
func =table[op]
print(func(2,3))