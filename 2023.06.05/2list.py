#두 개의 리스트가 주어졌을 때, 두 리스트에 공통으로 포함된 요소를 모두 담은 리스트를 반환하는 프로그램을 작성하시오.

#리스트A: 임의의 길이와 요소를 가진 리스트
#리스트B: 임의의 길이와 요소를 가진 리스트
list1 = set([1, 2, 3, 4, 5])
list2 = set([2, 4, 6, 8, 10])
print(list(list1 & list2))

