#사과 쇼핑몰"에서 사과를 구매할 때, 총 가격을 계산하는 프로그램을 작성하세요.

#사용자로부터 사과의 개수와 가격, 그리고 부가세율을 입력받아, 총 가격을 계산하는 프로그램을 작성하세요.
appleNum=int(input("사과의 개수를 입력해주세요."))
appleValue=int(input("가격을 입력해주세요."))
vat=float(input("부가세(%)율을 입력해주세요."))/100

sum = appleNum * appleValue * vat
print(f"총가격은 {sum}입니다.")
