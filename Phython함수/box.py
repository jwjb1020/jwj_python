#두 개의 매개변수 n, m을 전달받아 m x n개의 * 상자를 출력하는 프로그램을 함수로 작성
def box(n,m):
    for i in range(n):
        print()
        for j in range(m):
            print("*",end=" ")

box(2,4)       