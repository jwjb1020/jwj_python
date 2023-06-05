#주어진 문자열에서 각 알파벳의 빈도수를 구하는 프로그램을 작성하시오.
#text = "Hello, world!"

#결과값
#{'H': 1, 'e': 1, 'l': 3, 'o': 2, ',': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1, '!': 1}

text = input("문장을 입력하세요")
d = {}
for char in text:
    if char not in d:
        d[char] = 1
    else: 
        d[char] +=1
print(d)            