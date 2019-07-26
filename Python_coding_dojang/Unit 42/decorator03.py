### Unit 42. 데코레이터 사용하기
## 42.3 매개변수가 있는 데코레이터 만들기

## 이번에는 매개변수가 있는 데코레이터를 만들어보겠습니다.
## 이런 방식의 데코레이터는 값을 지정해서 동작을 바꿀 수 있습니다.
## 다음은 함수의 반환값이 특정 수의 배수인지 확인하는 데코레이터입니다.

def is_multiple(x):  # 데코레이터가 사용할 매개변수를 지정
    def real_decorator(func):  # 호출할 함수를 매개변수로 받음
        def wrapper(a, b):  # 호출할 함수의 매개변수와 똑같이 지정
            r = func(a, b)  # func를 호출하고 반환값을 변수에 저장
            if r % x == 0:  # func의 반환값이 x의 배수인지 확인
                print('{0}의 반환값은 {1}의 배수입니다.'.format(func.__name__, x))
            else:
                print('{0}의 반환값은 {1}의 배수가 아닙니다.'.format(func.__name__, x))
            return r  # func의 반환값을 반환

        return wrapper  # wrapper 함수 반환

    return real_decorator  # real_decorator 함수 반환


@is_multiple(3)  # @데코레이터(인수)
def add(a, b):
    return a + b


print(add(10, 20))
print(add(2, 5))


# 참고 | 매개변수가 있는 데코레이터를 여러 개 지정하기
# 매개변수가 있는 데코레이터를 여러 개 지정할 때는
# 다음과 같이 인수를 넣은 데코레이터를 여러 줄로 지정해줍니다.

# @데코레이터1(인수)
# @데코레이터2(인수)
# def 함수이름():
#     코드

@is_multiple(3)
@is_multiple(7)
def add(a, b):
    return a + b


add(10, 20)

# @을 사용하지 않았을 때는 다음 코드와 동작이 같습니다.
decorated_add = is_multiple(3)(is_multiple(7)(add))
decorated_add(10, 20)


# 참고 | 원래 함수 이름이 안나온다면?
# 데코레이터를 여러 개 사용하면 데코레이터에서 반환된 wrapper 함수가 다른 데코레이터로 들어갑니다.
# 따라서 함수의 __name__을 출력해보면 wrapper가 나옵니다.

import functools


def is_multiple(x):
    def real_decorator(func):
        @functools.wraps(func)  # @functools.wraps에 func를 넣은 뒤 wrapper 함수 위에 지정
        def wrapper(a, b):
            r = func(a, b)
            if r % x == 0:
                print('{0}의 반환값은 {1}의 배수입니다.'.format(func.__name__, x))
            else:
                print('{0}의 반환값은 {1}의 배수가 아닙니다.'.format(func.__name__, x))
            return r

        return wrapper

    return real_decorator


@is_multiple(3)
@is_multiple(7)
def add(a, b):
    return a + b


add(10, 20)