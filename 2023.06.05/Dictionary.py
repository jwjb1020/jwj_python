days = {'January':31, 'February':28, 'March':31, 'April':30,'May':31, 'June':30, 'July':31, 'August':31,'September':30, 'October':31, 'November':30, 'December':31}
month = input("월을 입력하세요")
print(days[month.title()])
print("월을 알파벳 순서로 출력")
days_key =days.keys()
print(sorted(days_key))
print("일수가 31인 월을 모두 출력하라")
for mon in days:
    if days[mon] == 31:
        print(mon,end=" ")
print()        
print("월의 일수를 기준으로 오름차순으로 키 벨류 쌍을 출력")
days_item = days.items()
r_days = [(day, month) for (month, day) in days_item]
r_days.sort()
days2 = [(month,day) for (day, month) in r_days]
print(days2)
print("사용자가 월을 3자리만 입력하면 월의 일수을 출려하라(Jan,Feb 등)")
mon = input("월을 세자리로 입력해주세요")
for m in days:
    if m[0:3] == mon.title():
        print(days[m])        