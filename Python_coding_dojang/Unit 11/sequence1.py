### Unit 11. 시퀀스 자료형 활용하기
## 11.1 시퀀스 자료형의 공통 기능 사용하기
## 11.1.1  특정 값이 있는지 확인하기
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(30 in a)
print(100 in a)

a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(100 not in a)
print(30 not in a)

print(43 in (38, 76, 43, 62, 19))
print(1 in range(10))
print('p' in 'Hello, Python')


## 11.1.2  시퀀스 객체 연결하기
## 시퀀스객체1 + 시퀀스객체2
a = [0, 10, 20, 30]
b = [9, 8, 7, 6]
print(a + b)

print(list(range(0, 10)) + list(range(10, 20)))
print(tuple(range(0, 10)) + tuple(range(10, 20)))
print('Hello, ' + 'world!')

# 참고 | 문자열에 숫자 연결하기
# 문자열' + str(정수)
# 문자열' + str(실수)
print('Hello, ' + str(10))      # str을 사용하여 정수를 문자열로 변환
print('Hello, ' + str(1.5))     # str을 사용하여 실수를 문자열로 변환


## 11.1.3  시퀀스 객체 반복하기
## 시퀀스객체 * 정수
## 정수 * 시퀀스객체
print([0, 10, 20, 30] * 3)

print(list(range(0, 5, 2)) * 3)
print('Hello, ' * 3)