islogined = True

def check_login():
    if islogined:
        return True

# 전처리, 후처리 로직이 너무 길다!
# 중복되는 코드가 너무 많이 발생!!! -> 이걸 어떻게 없앨까?
# 파이썬의 데코레이터를 활용한다!

# myFunc: 핵심 로직을 구현한 함수
def myFunc():
    # 로그인 되어있는지 여부를 확인
    check_login()

    print('myfunc')

    #로직이 끝났다! 안내문

def my_decorator(func):
    def wrapper():
        # 전처리
        if not islogined:
            print('로그인 하고 오라!')
            return
        
        func()
        # 후처리
        print('로직 끝남ㅇㅅㅇ')
    return wrapper

@my_decorator
def myFunc():
    print('myfunc')

