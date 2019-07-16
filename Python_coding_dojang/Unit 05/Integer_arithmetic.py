### Unit 5. 숫자 계산하기
## 5.1 정수 계산하기

## 5.1.1 사칙연산
print(1 + 1)
print(1 - 2)
print(2 * 2)
print(5 / 2)
print(4 / 2)


## 5.1.2 나눗셈 후 소수점 이하를 버리는 // 연산자
print(5 // 2)
print(4 // 2)
print(5.2 // 2)
print(4 // 2.0)
print(4.1 // 2.1)


## 5.1.3 나눗셈 후 나머지를 구하는 % 연산자
print(5 % 2)


## 5.1.4 거듭제곱을 구하는 ** 연산자
print(2 ** 10)


## 5.1.5 값을 정수로 만들기
print(int(3.3))
print(int(5 / 2))
print(int('10'))


## 5.1.6 객체의 자료형 알아내기
print(type(10))


## 참고 | 몫과 나머지를 함께 구하기
print(divmod(5, 2))

quotient, remainder = divmod(5, 2)
print(quotient, remainder)
print(type(quotient))


## 참고 | 진수, 8진수, 16진수
# 2진수 : 숫자 앞에 0b를 붙이며 0과 1을 사용합니다.
# 8진수 : 숫자 앞에 0o(숫자 0과 소문자 o)를 붙이며 0부터 7까지 사용합니다.
# 16진수: 숫자 앞에 0x 또는 0X를 붙이며 0부터 9, A부터 F까지 사용합니다(소문자 a부터 f도 가능).
print(0b110)
print(0o10)
print(0xF)
