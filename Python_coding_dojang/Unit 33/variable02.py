### Unit 33. 클로저 사용하기
## 33.2 함수 안에서 함수 만들기

## def 함수이름1():
##     코드
##     def 함수이름2():
##         코드

def print_hello():
    hello = 'Hello, world!'
    def print_message():
        print(hello)
    print_message()

print_hello()


## 33.2.1  지역 변수의 범위
def print_hello():
    hello = 'Hello, world!'
    def print_message():
        print(hello)    # 바깥쪽 함수의 지역 변수를 사용


## 33.2.2  지역 변수 변경하기
def A():
    x = 10      # A의 지역 변수 x

    def B():
        x = 20  # x에 20 할당

    B()
    print(x)    # A의 지역 변수 x 출력

A()


# nonlocal 지역변수
def A():
    x = 10          # A의 지역 변수 x

    def B():
        nonlocal x  # 현재 함수의 바깥쪽에 있는 지역 변수 사용
        x = 20      # A의 지역 변수 x에 20 할당

    B()
    print(x)        # A의 지역 변수 x 출력

A()



## 33.2.3  nonlocal이 변수를 찾는 순서
## nonlocal은 현재 함수의 바깥쪽에 있는 지역 변수를 찾을 때
# 가장 가까운 함수부터 먼저 찾습니다
def A():
    x = 10
    y = 100

    def B():
        x = 20

        def C():
            nonlocal x
            nonlocal y
            x = x + 30
            y = y + 300
            print(x)
            print(y)

        C()
    B()
A()


## 33.2.4  global로 전역 변수 사용하기
## 함수가 몇 단계든 상관없이 global 키워드를 사용하면 무조건 전역 변수를 사용하게 됩니다.
x = 1

def A():
    x = 10

    def B():
        x = 20

        def C():
            global x
            x = x + 30
            print(x)

        C()
    B()
A()