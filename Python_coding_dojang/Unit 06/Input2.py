### Unit 6. 변수와 입력 사용하기
## 6.4 입력 값을 변수 두 개에 저장하기


# 변수1, 변수2 = input().split()
# 변수1, 변수2 = input().split('기준문자열')
# 변수1, 변수2 = input('문자열').split()
# 변수1, 변수2 = input('문자열').split('기준문자열')


a, b = input('문자열 두 개를 입력하세요: ').split()    # 입력받은 값을 공백을 기준으로 분리

print(a)
print(b)


## 6.4.1 두 숫자의 합 구하기
a, b = input('숫자 두 개를 입력하세요: ').split()    # 입력받은 값을 공백을 기준으로 분리
 
print(a + b)


## 6.4.2 입력 값을 정수로 변환하기
a, b = input('숫자 두 개를 입력하세요: ').split()    # 입력받은 값을 공백을 기준으로 분리
a = int(a)    # 변수를 정수로 변환한 뒤 다시 저장
b = int(b)    # 변수를 정수로 변환한 뒤 다시 저장
 
print(a + b)
print(int(a) + int(b))


## 6.4.3 map을 사용하여 정수로 변환하기
# 변수1, 변수2 = map(int, input().split())
# 변수1, 변수2 = map(int, input().split('기준문자열'))
# 변수1, 변수2 = map(int, input('문자열').split())
# 변수1, 변수2 = map(int, input('문자열').split('기준문자열'))

a, b = map(int, input('숫자 두 개를 입력하세요: ').split())
 
print(a + b)


## 6.4.4 입력받은 값을 콤마를 기준으로 분리하기
a, b = map(int, input('숫자 두 개를 입력하세요: ').split(',')) # 입력받은 값을 콤마를 기준으로 분리
 
print(a + b)