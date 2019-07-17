### Unit 15. elif를 사용하여 여러 방향으로 분기하기
## 15.1 elif 사용하기
## if 조건식:
##      코드1
## elif 조건식:
##      코드2

x = 20
if x == 10:
    print('10입니다')
elif x == 20:
    print('20입니다')


## 15.1.1  if, elif, else를 모두 사용하기
## if 조건식:
##     코드1
## elif 조건식:
##     코드2
## else:
##     코드3

x = 30
 
if x == 10:             # x가 10일 때
    print('10입니다.')
elif x == 20:           # x가 20일 때
    print('20입니다.')
else:                   # 앞의 조건식에 모두 만족하지 않을 때
    print('10도 20도 아닙니다.')



## 15.1.2  음료수 자판기 만들기
button = int(input())

if button == 1:
    print('콜라')
elif button == 2:
    print('사이다')
elif button == 3:
    print('환타')
else:
    print('제공하지 않는 메뉴')

