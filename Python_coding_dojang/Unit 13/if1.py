### Unit 13. if 조건문으로 특정 조건일 때 코드 실행하기
## 13.1 if 조건문 사용하기
## if 조건식:
##     코드
x = 10
if x == 10:
    print('10입니다')



## 13.1.1  if 조건문의 기본 형태와 실행 흐름 알아보기
## 보통 if의 조건식이 만족하면 참( True), 만족하지 않으면 거짓(False)이라고 부릅니다.



## 13.1.2  if 조건문을 사용할 때 주의할 점
# if x = 10: 
#   File "<stdin>", line 1
#     if x = 10:
#          ^
# SyntaxError: invalid syntax 


## 13.1.3  if 조건문에서 코드를 생략하기
x = 10
if x == 10:
    pass

if x == 10:
    pass    # TODO: x가 10일 때 처리가 필요함

# 참고 | TODO
# TODO는 해야 할 일이라는 뜻인데 보통 주석에 넣습니다.