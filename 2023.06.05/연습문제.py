L = [1, 2, 3]
M = [4, 5, 6]
N = []

for i in range(len(L)):
    N.append(L[i] + M[i])

print(N)

num_list = input("5개의 숫자를 입력하세요.(구분 : 띄어쓰기)").split()
result = "+".join(num_list)
print(result)