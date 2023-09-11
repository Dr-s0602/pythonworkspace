# chap03_str.py
# 파이썬 에서 문자열 다루기

# 파이썬 에서 문자열(str)은 시퀀스(sequence: 순차 자료형)로 취급됨
# 시퀀스 자료 형은 값의 순번(index)이 매겨짐, 0부터 시작됨

# 문자 선택 연산자 (인덱싱) : 문자변수[index] => java.chatAt()

ss = 'Hi,-python'
print('첫번째 글자 : ', ss[0])
print('다섯번째 글자 : ', ss[4])
print('뒤에서 첫번째  : ', ss[-1])

# 문자열 범위 선택 연산자 (슬라이싱): 문자열 값 부분 추출시 사용 => java.subString()
# 문자변수[시작인덱스 : 끝인덱스-1 [: 간격]]
print('슬라이싱 연습 ',ss[0:2])
print(ss[0:5:2])

#슬라이싱을 이용해서 문자열을 역순으로 정렬할 수도 있음

print(ss[::-1]) #시작과 끝이 없으면 모든 글자임, 뒤에서 부터 추출됨

#슬라이싱과 연결연산(+)을 혼합해서 사용 가능함
n1 = 'abcdef'
n2 = '12345'
n3 = n1[0:3] + n2[1:] #끝 인덱스 생략은 끝글자까지를 의미함
print(n3)

#문자열 반복 연산자 : * 반복할 횟수
print('hello'*3)

#문자 처리 내장함수
#upper(), lower() : 영문자 일때 대/소문자로 변환하는 함수
tt = 'apple'
print(tt)
#파이썬에서는 기록된 문자값은 변경 못함
# tt[0] = b
#해결 : 제공되는 관련 함수를 사용하면 됨
print(tt.upper())

tt2 = 'BANANA'
print(tt2.lower())

#swapcase(),capitalize()

tt3 = "tEst stR pyTHOn"
print(tt3)
print(tt3.swapcase()) #소문자는 대문자로, 대문자는 소문자로 변환 함수
print(tt3.capitalize()) # 문장의 첫글자를 대문자로 변환, 나머지는 소문자로

#title() : 각 단어의 첫글자를 대문자로
print(tt3.title())

tt4 = '    test str values     '
#strip(), lstrip(), rstrip()
print('|',tt4,'|',sep='')

print('|',tt4.strip(),'|',sep='')
#문자 앞뒤의 공백 제거함
print('|',tt4.lstrip(),'|',sep='')
# 문자 앞(왼쪽)의 공백 제거함
print('|',tt4.rstrip(),'|',sep='')
# 문자 뒤(오른쪽)의 공백 제거함

#split(), splitlines()

tt5 = 'abc-def-ghi-f'

print(tt5)
print(tt5.split('-')) #지정하는 문자를 기준으로 문자값을 분리함
#여려 개의 문자들로 분리됨 => 리스트 형식이 결과형임

#splitlines() : 줄(line)단위로 분리해서 리스트를 리턴함
tt6 = ''' python
java
c++
javascript
'''
print(tt6)
print(tt6.splitlines())

#index(), find() 글자 위치(순번:인덱스) 조회
print(tt5.index('e')) #문자열 안에 있는 'e' 문자의 위치 조회
#없는 문자 조회하면 에러남

#print(tt5.index('k'))

print(tt5.find('e')) # 찾아낸 문자의 위치를 리턴
print(tt5.find('k')) # 찾아낼 문자가 없으면 -1

#이 외의 다른 문자 관련 함수들을 조회하려면
print(dir(str))
print(len(dir(str)))

# 문자열에 포멧(format)을 적용하여 코드 작성하는 방법
# 문자열 값 사이에 다른 종류의 값이나 변수를 적용하려고 할때 이용