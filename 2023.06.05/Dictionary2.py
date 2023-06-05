#전화번호가 8로 끝나는 사용자 이름을 출력하라
#이메일이 없는 사용자 이름을 출력하라
#사용자 이름을 입력하면 전화번호, 이메일을 출력하라. 이름이 없으면 '이름이 없습니다'라는 메시지를 출력하라
d=[{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},{'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},{'name':'Princess', 'phone':'555-3141', 'email':''},{'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]
for people in d:
    if people['phone'][7] == '8':
        print(people['name'])
print('='*30)  

s_name = input("찾을 이름을 입력하세요.")
flag =1
for people in d:
    if people['name'] == s_name:
        print(people['phone'],people['email'])
        flag = 0
if flag ==1:
    print("없는 이름입니다.")        