### Unit 42. 데코레이터 사용하기
## 42.5 클래스로 매개변수와 반환값을 처리하는 데코레이터 만들기

## 함수의 매개변수를 출력하는 데코레이터입니다
## (여기서는 위치 인수와 키워드 인수를 모두 처리하는 가변 인수로 만들었습니다).

class Trace:
    def __init__(self, func):             # 호출할 함수를 인스턴스의 초깃값으로 받음
        self.func = func                  # 호출할 함수를 속성 func에 저장

    def __call__(self, *args, **kwargs):  # 호출할 함수의 매개변수를 처리
        r = self.func(*args, **kwargs)    # self.func에 매개변수를 넣어서 호출하고 반환값을 변수에 저장
        print('{0}(args={1}, kwargs={2}) -> {3}'.format(self.func.__name__, args, kwargs, r))
                                          # 매개변수와 반환값 출력
        return r                          # self.func의 반환값을 반환


@Trace                                    # @데코레이터
def add(a, b):
    return a + b


print(add(10, 20))
print(add(a=10, b=20))



## 42.5.1  클래스로 매개변수가 있는 데코레이터 만들기
## 함수의 반환값이 특정 수의 배수인지 확인하는 데코레이터입니다.
class IsMultiple:
    def __init__(self, x):       # 데코레이터가 사용할 매개변수를 초깃값으로 받음
        self.x = x               # 매개변수를 속성 x에 저장

    def __call__(self, func):    # 호출할 함수를 매개변수로 받음
        def wrapper(a, b):       # 호출할 함수의 매개변수와 똑같이 지정(가변 인수로 작성해도 됨)
            r = func(a, b)       # func를 호출하고 반환값을 변수에 저장
            if r % self.x == 0:  # func의 반환값이 self.x의 배수인지 확인
                print('{0}의 반환값은 {1}의 배수입니다.'.format(func.__name__, self.x))
            else:
                print('{0}의 반환값은 {1}의 배수가 아닙니다.'.format(func.__name__, self.x))
            return r             # func의 반환값을 반환

        return wrapper           # wrapper 함수 반환


@IsMultiple(3)                   # 데코레이터(인수)
def add(a, b):
    return a + b


print(add(10, 20))
print(add(2, 5))