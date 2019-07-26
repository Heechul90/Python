### Unit 42. 데코레이터 사용하기
## 42.2 매개변수와 반환값을 처리하는 데코레이터 만들기

## 매개변수와 반환값을 처리하는 데코레이터는 어떻게 만드는지 알아보겠습니다.
## 다음은 함수의 매개변수와 반환값을 출력하는 데코레이터입니다.

def trace(func):             # 호출할 함수를 매개변수로 받음
    def wrapper(a, b):       # 호출할 함수 add(a, b)의 매개변수와 똑같이 지정
        r = func(a, b)       # func에 매개변수 a, b를 넣어서 호출하고 반환값을 변수에 저장
        print('{0}(a={1}, b={2}) -> {3}'.format(func.__name__, a, b, r))  # 매개변수와 반환값 출력
        return r             # func의 반환값을 반환

    return wrapper           # wrapper 함수 반환


@trace                       # @데코레이터
def add(a, b):               # 매개변수는 두 개
    return a + b             # 매개변수 두 개를 더해서 반환


print(add(10, 20))


## 42.2.1  가변 인수 함수 데코레이터
## ef add(a, b):는 매개변수의 개수가 고정된 함수입니다.
## 그러면 매개변수(인수)가 고정되지 않은 함수는 어떻게 처리할까요?
## 이때는 wrapper 함수를 가변 인수 함수로 만들면 됩니다.

def trace(func):                       # 호출할 함수를 매개변수로 받음
    def wrapper(*args, **kwargs):      # 가변 인수 함수로 만듦
        r = func(*args, **kwargs)      # func에 args, kwargs를 언패킹하여 넣어줌
        print('{0}(args={1}, kwargs={2}) -> {3}'.format(func.__name__, args, kwargs, r))
                                       # 매개변수와 반환값 출력
        return r                       # func의 반환값을 반환

    return wrapper                     # wrapper 함수 반환


@trace                                 # @데코레이터
def get_max(*args):                    # 위치 인수를 사용하는 가변 인수 함수
    return max(args)


@trace                                 # @데코레이터
def get_min(**kwargs):                 # 키워드 인수를 사용하는 가변 인수 함수
    return min(kwargs.values())


print(get_max(10, 20))
print(get_min(x=10, y=20, z=30))


# 참고 | 메서드에 데코레이터 사용하기
# 인스턴스 메서드는 항상 self를 받으므로
# 데코레이터를 만들 때도 wrapper 함수의 첫 번째 매개변수는 self로 지정해야 합니다(클래스 메서드는 cls).
# 마찬가지로 func를 호출할 때도 self와 매개변수를 그대로 넣어야 합니다.

def trace(func):
    def wrapper(self, a, b):  # 호출할 함수가 인스턴스 메서드이므로 첫 번째 매개변수는 self로 지정
        r = func(self, a, b)  # self와 매개변수를 그대로 넣어줌
        print('{0}(a={1}, b={2}) -> {3}'.format(func.__name__, a, b, r))  # 매개변수와 반환값 출력
        return r  # func의 반환값을 반환

    return wrapper


class Calc:
    @trace
    def add(self, a, b):  # add는 인스턴스 메서드
        return a + b


c = Calc()
print(c.add(10, 20))