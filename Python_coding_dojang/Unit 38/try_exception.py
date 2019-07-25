### Unit 38. 예외 처리 사용하기

def ten_div(x):
    return 10 / x

ten_div(2)
ten_div(0)

## 38.1 try except로 사용하기
# try:
#     실행할 코드
# except:
#     예외가 발생했을 때 처리하는 코드

try:
    x = int(input('나눌 숫자를 입력하세요.: '))
    y = 10 / x
    print(y)
except:                          # 예외가 발생했을 때 실행됨
    print('예외가 발생했습니다.')


## 38.1.1  특정 예외만 처리하기
## 이번에는 except에 예외 이름을 지정해서
## 특정 예외가 발생했을 때만 처리 코드를 실행하도록 만들어보겠습니다.

# try:
#     실행할 코드
# except 예외이름:
#     예외가 발생했을 때 처리하는 코드

y = [10, 20, 30]

try:
    index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
    print(y[index] / x)
except ZeroDivisionError:            # 숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
    print('숫자를 0으로 나눌 수 없습니다.')
except IndexError:                   # 범위를 벗어난 인덱스에 접근하여 에러가 발생했을 때 실행됨
    print('잘못된 인덱스입니다.')



## 38.1.2  예외의 에러 메시지 받아오기
## 특히 except에서 as 뒤에 변수를 지정하면 발생한 예외의 에러 메시지를 받아올 수 있습니다.

# try:
#     실행할 코드
# except 예외 as 변수:
#     예외가 발생했을 때 처리하는 코드

y = [10, 20, 30]

try:
    index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
    print(y[index] / x)
except ZeroDivisionError as e:              # as 뒤에 변수를 지정하면 에러를 받아옴
    print('숫자를 0으로 나눌 수 없습니다.', e)  # e에 저장된 에러 메시지 출력
except IndexError as e:
    print('잘못된 인덱스입니다.', e)



# 참고 | 예외 계층
