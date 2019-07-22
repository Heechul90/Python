### Unit 29. 함수 사용하기
## 29.5 함수의 호출 과정 알아보기

def mul(a, b):
    c = a * b
    return c

def add(a, b):
    c = a + b
    print(c)
    d = mul(a, b)
    print(d)

x = 10
y = 20
add(x, y)