### Unit 8. 불과 비교, 논리 연산자 알아보기
## 8.2 논리 연산자 사용하기


# a and b
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# a or b
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# not x
print(not True)
print(not False)

print(not True and False or not False)



## 8.2.1 논리 연산자와 비교 연산자를 함께 사용하기
print(10 == 10 and 10 != 5)    # True and True
print(10 > 5 or 10 < 3)        # True or False
print(not 10 > 5)              # not True
print(not 1 is 1.0)            # not False

# 참고 | 정수, 실수, 문자열을 불로 만들기
print(bool(1))
print(bool(0))
print(bool(1.5))
print(bool('False'))

# 참고 | 단락 평가
# 첫 번째 값이 거짓이므로 두 번째 값은 확인하지 않고 거짓으로 결정
print(False and True)     # False
print(False and False)    # False

# 첫 번째 값이 참이므로 두 번째 값은 확인하지 않고 참으로 결정
print(True or True)       # True
print(True or False)      # True

print(True and 'Python')
print('Python' and True)
print('Python' and False)
print(False and 'Python')
print(0 and 'Python')            # 0은 False이므로 and 연산자는 두 번째 값을 평가하지 않음
print(True or 'Python')
print('Python' or True)
print(False or 'Python')
print(0 or False)
