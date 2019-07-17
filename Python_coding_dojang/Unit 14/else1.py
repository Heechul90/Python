### Unit 14. else를 사용하여 두 방향으로 분기하기
## 14.1 else 사용하기
## if 조건식:
##      코드1
## else:
##      코드2
x = 5
if x == 10:
    print('10입니다')
else:
    print('10이 아닙니다')


## 14.1.1  if와 else의 기본 형태와 실행 흐름 알아보기

# 참고 | 변수에 값 할당을 if, else로 축약하기
x = 5
if x == 10:
    y = x
else:
    y = 0

print(y)


x = 5
y = x if x == 10 else 0
print(y)