# 식별자 : 프로그래머가 지어 주는 이름을 말함
# 변수 (variable) : 프로그램 구동시 메모리(RAM)에 값 기록 하는 공간(방)
# 함수 (function) : 반복 사용되 는 코드를 분리 작성 해서 이름을 붙여 준 것(코드의 조각 코드들)
# 모듈 (module) : 함수 들을 따로 모아 놓은 파일
# 클래스 (class) :  파이썬은 객체 지향형 스크립트 언어임

#파이썬의 이름 작성 규칙 (식별자의 조건 : Naming Rule)
#1. 대소문자 구분함 : name 과 Name 은 다른 이름임

NAME = '홍길동'
name = '이순신'
Name = '황지니'

print(NAME)
print(name)
print(Name)

# 2. 이름의 첫글자에 숫자 사용 못 함 : 1num (에러)
# 1num = 100
# print(1num)

# 3. 이름의 첫글자는 문자 또는 _(언더스코어)만 사용할 수 있음
_score = 100.0
print(_score)

# 4. 숫자는 이림의 중간 위치나 끝에 사용할 수 있음 : num1,first1_menu
num1 = 10
num2 = 20
print(num1 > num2)

# 5. 언더스코어를 제외한 특수문자, 공백 사용 못함
# &menu,all*.one num :  에러
# num& = 1
# print(num&)

# 6. 예약어(프로그램언어가 별도로 사용하려고 정해놓은 단어들)는 이름으로 사용할수 없음
# true = 1 (ok), True = 1 (error)

# 파이썬이 제공하는 예약어 확인
# keyword 모듈에서 제공함 : import 해서 사용함

import keyword

print(keyword.kwlist)

