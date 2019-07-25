### Unit 38. 예외 처리 사용하기
## 38.2 else와 finally 사용하기
## 이번에는 예외가 발생하지 않았을 때 코드를 실행하는 else를 사용
## else는 except 바로 다음에 와야 하며 except를 생략할 수 없음

# try:
#     실행할 코드
# except:
#     예외가 발생했을 때 처리하는 코드
# else:
#     예외가 발생하지 않았을 때 실행할 코드

try:
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10 / x
except ZeroDivisionError:       # 숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
    print('숫자를 0으로 나눌 수 없습니다.')
else:                           # try의 코드에서 예외가 발생하지 않았을 때 실행됨
    print(y)



## 38.2.1  예외와는 상관없이 항상 코드 실행하기
## 예외 발생 여부와 상관없이 항상 코드를 실행하는 finally를 사용
## finally는 except와 else를 생략할 수 있음

# try:
#     실행할 코드
# except:
#     예외가 발생했을 때 처리하는 코드
# else:
#     예외가 발생하지 않았을 때 실행할 코드
# finally:
#     예외 발생 여부와 상관없이 항상 실행할 코드

try:
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10 / x
except ZeroDivisionError:    # 숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
    print('숫자를 0으로 나눌 수 없습니다.')
else:                        # try의 코드에서 예외가 발생하지 않았을 때 실행됨
    print(y)
finally:                     # 예외 발생 여부와 상관없이 항상 실행됨
    print('코드 실행이 끝났습니다.')


# 참고 | try 안에서 만든 변수는 try 바깥에서 사용할 수 있나요?
# try는 함수가 아니므로 스택 프레임을 만들지 않습니다
# 따라서 try 안에서 변수를 만들더라도 try 바깥에서 사용할 수 있습니다.
# 물론 except, else, finally에서도 사용할 수 있습니다.