### Unit 14. else를 사용하여 두 방향으로 분기하기
## 14.3 if 조건문의 동작 방식 알아보기
if True:
    print('참')      # True는 참
else:
    print('거짓')
 
if False:
    print('참')
else:
    print('거짓')    # False는 거짓
 
if None:
    print('참')
else:
    print('거짓')    # None은 거짓



## 14.3.1  if 조건문에 숫자 지정하기
if 0:
    print('참')
else:
    print('거짓')  # 0은 거짓
 
if 1:
    print('참')    # 1은 참
else:
    print('거짓')
 
if 0x1F:           # 16진수
    print('참')    # 0x1F는 참
else:
    print('거짓')
 
if 0b1000:         # 2진수
    print('참')    # 0b1000은 참
else:
    print('거짓')
 
if 13.5:           # 실수
    print('참')    # 13.5는 참
else:
    print('거짓')



## 14.3.2  if 조건문에 문자열 지정하기
if 'Hello':          # 문자열
    print('참')      # 문자열은 참
else:
    print('거짓')
 
if '':               # 빈 문자열
    print('참')
else:
    print('거짓')    # 빈 문자열은 거짓



# 참고 | 0, None, 빈 문자열을 not으로 뒤집으면?
if not 0:
    print('참')    # not 0은 참
 
if not None:
    print('참')    # None은 참
 
if not '':
    print('참')    # not 빈 문자열은 참