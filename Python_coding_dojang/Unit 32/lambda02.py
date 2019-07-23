### Unit 32. 람다 표현식 사용하기
## 32.2 람다 표현식과 map, filter, reduce 함수 활용하기

## 32.2.1  람다 표현식에 조건부 표현식 사용하기
## lambda 매개변수들: 식1 if 조건식 else 식2

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(map(lambda x: str(x) if x % 3 == 0 else x, a))

## list(map(lambda x: str(x) if x % 3 == 0, a))
## SyntaxError: invalid syntax

## lambda 매개변수들: 식1 if 조건식1 else 식2 if 조건식2 else 식3
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(map(lambda x: str(x) if x == 1 else float(x) if x == 2 else x + 10, a))

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def f(x):
    if x == 1:
        return str(x)
    elif x == 2:
        return float(x)
    else:
        return x + 10

list(map(f, a))


## 32.2.2  map에 객체를 여러 개 넣기
a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]

list(map(lambda x, y: x * y, a, b))


## 32.2.3  filter 사용하기
## filter(함수, 반복가능한객체)
def f(x):
    return x > 5 and x < 10

a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]

list(filter(f, a))


a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
list(filter(lambda x: x > 5 and x < 10, a))


## 32.2.4  reduce 사용하기
## from functools import reduce
## reduce(함수, 반복가능한객체)
def f(x, y):
    return x + y

a = [1, 2, 3, 4, 5]

from functools import reduce
reduce(f, a)


a = [1, 2, 3, 4, 5]
from functools import reduce

reduce(lambda x, y: x + y, a)


# 참고 | map, filter, reduce와 리스트 표현식
# 리스트(딕셔너리, 세트) 표현식으로 처리할 수 있는 경우에는
# map, filter와 람다 표현식 대신 리스트 표현식을 사용하는 것이 좋습니다.
a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
[i for i in a if i > 5 and i < 10]

# reduce(lambda x, y: x + y, a)는 다음과 같이 for 반복문으로 표현할 수 있습니다.
a = [1, 2, 3, 4, 5]
x = a[0]
for i in range(len(a) -1):
    x = x + a[i + 1]

x