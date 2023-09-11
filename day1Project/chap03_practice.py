'''
회원 이름
회원아이디
패스워드
나이
키
출력
이름 회원의 아이디는 아이디이고, 암호는 pass**** 입니다.
나이는 나이세 이고 키는 키.1 cm 입니다.

암호는 첫글자부터 4글자만 슬라이싱 나머지 글자에 맞게 *
키는 소숫점 아래 첫자리만 출력

'''

member_name = input('회원 이름 : ')
member_id = input('회원 아이디 : ')
member_pwd = input('패스워드 : ')
age = int(input('나이 : '))
height = float(input('키 : '))
# password = member_pwd[0:4] + '*************'[0:len(member_pwd)-4]
password = member_pwd[0:4] + ('*' * (len(member_pwd)-4))
print(f'{member_name} 회원의 아이디는 {member_id}이고, 암호는 {password} 입니다.')
print(f'나이는 {age}세이고, 키는 {height:0.1f}cm 입니다.')
