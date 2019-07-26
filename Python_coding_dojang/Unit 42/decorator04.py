### Unit 42. 데코레이터 사용하기
## 42.4 클래스로 데코레이터 만들기

## 이번에는 클래스로 데코레이터를 만드는 방법을 알아보겠습니다.
## 특히 클래스를 활용할 때는 인스턴스를 함수처럼 호출하게 해주는 __call__ 메서드를 구현해야 합니다.

class Trace:
    def __init__(self, func):                  # 호출할 함수를 인스턴스의 초깃값으로 받음
        self.func = func                       # 호출할 함수를 속성 func에 저장

    def __call__(self):
        print(self.func.__name__, '함수 시작')  # __name__으로 함수 이름 출력
        self.func()                            # 속성 func에 저장된 함수를 호출
        print(self.func.__name__, '함수 끝')


@Trace                # @데코레이터
def hello():
    print('hello')


hello()               # 함수를 그대로 호출


# 참고로 클래스로 만든 데코레이터는 @을 지정하지 않고,
# 데코레이터의 반환값을 호출하는 방식으로도 사용할 수 있습니다.

def hello():  # @데코레이터를 지정하지 않음
    print('hello')


trace_hello = Trace(hello)  # 데코레이터에 호출할 함수를 넣어서 인스턴스 생성
trace_hello()  # 인스턴스를 호출. __call__ 메서드가 호출됨