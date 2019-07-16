### Unit 8. 불과 비교, 논리 연산자 알아보기
## 8.1 불과 비교 연산자 사용하기


print(True)
print(False)

## 8.1.1 비교 연산자의 판단 결과
print(3 > 1)


## 8.1.2 숫자가 같은지 다른지 비교하기
print(10 == 10)    # 10과 10이 같은지 비교
print(10 != 5)     # 10과 5가 다른지 비교


## 8.1.3 문자열이 같은지 다른지 비교하기
print('Python' == 'Python')
print('Python' == 'python')
print('Python' != 'python')


## 8.1.4 부등호 사용하기
print(10 > 20)     # 10이 20보다 큰지 비교
print(10 < 20)     # 10이 20보다 작은지 비교
print(10 >= 10)    # 10이 10보다 크거나 같은지 비교
print(10 <= 10)    # 10이 10보다 작거나 같은지 비교


## 8.1.5 객체가 같은지 다른지 비교하기
print(1 == 1.0)
print(1 is 1.0)
print(1 is not 1.0)

# 참고 | 정수 객체와 실수 객체가 서로 다른 것은 어떻게 확인하나요?
print(id(1))
print(id(1.0))

# 참고 | 값 비교에 is를 쓰지 않기
a = -5
print(a is -5)
a = -6
print(a is -6)
