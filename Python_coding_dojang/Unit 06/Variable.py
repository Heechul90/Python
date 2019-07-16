### Unit 6. 변수와 입력 사용하기
## 6.1 변수 만들기
x = 10
print(x)

y = 'Hello world'
print(y)


## 6.1.1 변수의 자료형 알아내기
print(type(x))
print(type(y))


## 6.1.2 변수 여러 개를 한 번에 만들기
x, y, z = 10, 20, 30
print(x)
print(y)
print(z)

x = y = z = 10
print(x)
print(y)
print(z)

# 변수 바꾸기
# 변수1, 변수2 = 변수2, 변수1
x, y = 10, 20
x, y = y, x
print(x)
print(y)


## 참고 | 변수 삭제하기
x = 10
del x


## 참고 | 빈 변수 만들기
x = None
print(x)