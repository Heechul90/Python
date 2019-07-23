### Unit 30. 함수에서 위치 인수와 키워드 인수 사용하기
## 30.1 위치 인수와 리스트 언패킹 사용하기
print(10, 20, 30)


##30.1.1  위치 인수를 사용하는 함수를 만들고 호출하기
def print_numbers(a, b, c):
    print(a)
    print(b)
    print(c)

print_numbers(10, 20, 30)


## 30.1.2  언패킹 사용하기
## 함수(*리스트)
## 함수(*튜플)
x = [10, 20, 30]
print_numbers(*x)

print_numbers(*[10, 20, 30])


## 30.1.3  가변 인수 함수 만들기
## def 함수이름(*매개변수):
##     코드
def print_numbers(*args):
    for arg in args:
        print(arg)

print_numbers(10)
print_numbers(10, 20, 30, 40)

x = [10]
print_numbers(*x)

y = [10, 20, 30, 40]
print_numbers(*y)

# 참고 | 고정 인수와 가변 인수를 함께 사용하기
# 고정 인수와 가변 인수를 함께 사용할 때는
# 다음과 같이 고정 매개변수를 먼저 지정하고,
# 그 다음 매개변수에 *를 붙여주면 됩니다.
def print_numbers(a, *args):
    print(a)
    print(args)

print_numbers(1)
print_numbers(1, 20, 30)
print_numbers(*[10, 20, 30])

# 단, 이때 def print_numbers(*args, a):처럼 *args가 고정 매개변수보다 앞쪽에 오면 안 됩니다.
# 매개변수 순서에서 *args는 반드시 가장 뒤쪽에 와야 합니다.