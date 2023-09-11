# 실행은 shift + f10

# 파이썬 에서 함수 만들기 : def  키워드 사용함
# def 함수명(매개 변수명):
# 들여 쓰기 함 함수의 코드 작성함

def print_hi(name):
    print(f'Hi,{name}')


def test_function():
    a = 1
    b = '1'
    c = 1.1
    d = True
    e = 99999999999999999999999999999999999999999999999999999999999999999999999
    print(type(a), type(b), type(c), type(d), type(e))


if __name__ == '__main__':
    print_hi('PyCharm')
    a = '안녕'
    b = '하세요'
    print(a + b)
    # 함수 실행 : 함수명(전달인자)
    test_function()
    print('main 종료')
