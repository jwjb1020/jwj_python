#숫자들이 들어있는 리스트에서 중복된 숫자를 제거하고, 남은 숫자들의 합을 계산하는 프로그램을 작성해보세요.
list = [1, 2, 2, 3, 3, 3, 4, 4, 5]
setlist = set(list)
sumList = sum(setlist)
print(f"Sum of unique number : {sumList}")