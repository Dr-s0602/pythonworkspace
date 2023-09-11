total_point = 12500

custom_name = input('고객 이름 : ')
price = int(input('결재 금액 : '))
point = (price/100)*5
total_point += int(point)

print('{}고객님의 사용금액은 {}원, 발생 포인트는 {} 현재 이용하실수 있는 누적 포인트는 {}점 입니다.'.format(custom_name,price,int(point),total_point))

#f-string 포매팅 사용
print(f'{custom_name}고객님의 사용금액은 {price}원, 발생 포인트는 {int(point)} 현재 이용하실수 있는 누적 포인트는 {int(total_point)}점 입니다.')
