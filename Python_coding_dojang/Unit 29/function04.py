### Unit 29. 함수 사용하기
## 29.4 함수에서 값을 여러 개 반환하기
## def 함수이름(매개변수):
##     return 반환값1, 반환값2

def add_sub(a, b):
    return a + b, a - b

x, y = add_sub(10, 20)
print(x)
print(y)

x = add_sub(10, 20)
print(x)

x, y = (30, -10)
print(x)
print(y)

# 참고 | 값 여러 개를 직접 반환하기
def one_two():
    return (1, 2)
1, 2

def one_two():
    return 1, 2    # return (1, 2)와 같음

def one_two():
    return [1, 2]

x, y = one_two()
print(x, y)
