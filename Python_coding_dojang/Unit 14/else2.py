### Unit 14. else를 사용하여 두 방향으로 분기하기
## 14.2 else와 들여쓰기
x = 5
if x == 10:
    print('10입니다')
else:
    print('x에 들어 있는 숫자는')
    print('10이 아닙니다')



x = 10
 
if x == 10:    # x가 10이라 조건식이 참
    print('10입니다.')    # 출력
else:
     print('x에 들어있는 숫자는')
print('10이 아닙니다.')    # 출력되지 않아야 하는데 출력됨


x = 10
 
if x == 10:    # x가 10이라 조건식이 참
    print('10입니다.')
else:
    print('x에 들어있는 숫자는')
 
print('10이 아닙니다.')