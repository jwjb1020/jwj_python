num = int(input("10진수 입력"))
binary = ""
while num>0:
    remainder =num%2
    binary= str(remainder)+binary
    num= num//2
print(binary) 
