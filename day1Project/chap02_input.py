#chap02_input.py

#파이썬에서 실행시 키ㅗ드로 값 입력받기
#input() 함수 사용함
# 변수명 = input('입력을 위한 메세지 문장')

# 입력을 위한 메세지 없이 실행 테스트
# num = input('숫자를 입력하세요 ')
# print('num : ',num,type(num))

#파이썬의 input() 함수로 입력되는 값은 모두 문자형(str) 이다
# print('더하기 확인 : ' , num + 100) #숫자와 문자는 계산할 수 없음

#숫자형으로 바꾸고자 한다면
# 정수는 int('정수문자'), 실수는 float('실수문자') 함수 사용함
# inum = int(num)
# print('imun = ',inum,type(inum))
# print(inum + 100)
#
# first = int(input('첫번째 정수 입력'))
# second = int(input('두번째 정수 입력'))
# print(first,'+',second,'=',first+second)
# print(first,'-',second,'=',first-second)
# print(first,'*',second,'=',first*second)
# print(first,'//',second,'=',first//second)
# print(first,'%',second,'=',first%second)
# print(first,'** 2=',first**2)
# print(second,'** 2=',second**2)

name = input('이름을 입력하세요')
age = int(input('나이를 입력하세요'))
gender = input('성별을 남|여 로 입력하세요')
height = float(input('키를 입력하세요'))
weight = float(input('몸무게를 입력하세요'))

print(name,'은 ',age,'세 이고 ',gender,'자이고 ',height,'cm 몸무게는 ',weight,'kg 입니다.' )
#format() 함수를 이요한 출력문
print('{}은 {}세 이고 {}자이고 {}cm, 몸무게는 {}kg 입니다.'.format(name,age,gender,height,weight))
#format() 함수와 순번을 적용한 출력문
print('{1}은 {0}세 이고 {2}자이고 {3}cm, 몸무게는 {4}kg 입니다.'.format(age,name,gender,height,weight))