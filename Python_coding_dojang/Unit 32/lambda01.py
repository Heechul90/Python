### Unit 32. 람다 표현식 사용하기
## 32.1 람다 표현식으로 함수 만들기
def plus_ten(x):
    return x + 10

plus_ten(1)

# lambda 매개변수들: 식
lambda x: x + 10

# lambda로 만든 익명 함수를 호출하려면 다음과 같이 람다 표현식을 변수에 할당해주면 됩니다.
plus_ten = lambda x: x + 10
plus_ten(1)


## 32.1.1  람다 표현식 자체를 호출하기
## (lambda 매개변수들: 식)(인수들)
(lambda x: x + 10)(1)


## 32.1.2  람다 표현식 안에서는 변수를 만들 수 없다
(lambda x: y = 10; x + y)(1)


y = 10
(lambda x: x + y)(1)


## 32.1.3  람다 표현식을 인수로 사용하기
def plus_ten(x):
    return x + 10

list(map(plus_ten, [1, 2, 3]))

list(map(lambda x: x + 10, [1, 2, 3]))


# 참고 | 람다 표현식으로 매개변수가 없는 함수 만들기
# 람다 표현식으로 매개변수가 없는 함수를 만들 때는
# lambda 뒤에 아무것도 지정하지 않고 :(콜론)을 붙입니다.
# 단, 콜론 뒤에는 반드시 반환할 값이 있어야 합니다.
(lambda : 1)()

x = 10
(lambda : x)()