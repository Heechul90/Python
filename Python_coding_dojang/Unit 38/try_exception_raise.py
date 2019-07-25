### Unit 38. 예외 처리 사용하기
## 38.3 예외 발생시키기

# 예외를 발생시킬 때는 raise에 예외를 지정하고
#  에러 메시지를 넣습니다(에러 메시지는 생략 할 수 있음).
# raise 예외('에러메시지')

try:
    x = int(input('3의 배수를 입력하세요: '))
    if x % 3 != 0:                                 # x가 3의 배수가 아니면
        raise Exception('3의 배수가 아닙니다.')       # 예외를 발생시킴
    print(x)
except Exception as e:                             # 예외가 발생했을 때 실행됨
    print('예외가 발생했습니다.', e)


## 38.3.1  raise의 처리 과정
## 이번에는 raise의 처리 과정을 알아보겠습니다.
## 다음은 함수 안에서 raise를 사용하지만 함수 안에는 try except가 없는 상태입니다
def three_multiple():
    x = int(input('3의 배수를 입력하세요: '))
    if x % 3 != 0:                              # x가 3의 배수가 아니면
        raise Exception('3의 배수가 아닙니다.')    # 예외를 발생시킴
    print(x)                                    # 현재 함수 안에는 except가 없으므로
                                                # 예외를 상위 코드 블록으로 넘김


try:
    three_multiple()
except Exception as e:  # 하위 코드 블록에서 예외가 발생해도 실행됨
    print('예외가 발생했습니다.', e)



## 38.3.2  현재 예외를 다시 발생시키기
## try except에서 처리한 예외를 다시 발생시키는 방법

# raise
# three_multiple 코드 블록의 예외를 다시 발생시킨 뒤 상위 코드 블록에서 예외를 처리
def three_multiple():
    try:
        x = int(input('3의 배수를 입력하세요: '))
        if x % 3 != 0:  # x가 3의 배수가 아니면
            raise Exception('3의 배수가 아닙니다.')  # 예외를 발생시킴
        print(x)
    except Exception as e:  # 함수 안에서 예외를 처리함
        print('three_multiple 함수에서 예외가 발생했습니다.', e)
        raise  # raise로 현재 예외를 다시 발생시켜서 상위 코드 블록으로 넘김


try:
    three_multiple()
except Exception as e:  # 하위 코드 블록에서 예외가 발생해도 실행됨
    print('스크립트 파일에서 예외가 발생했습니다.', e)



# 참고 | assert로 예외 발생시키기
# 예외를 발생시키는 방법 중에는 assert를 사용하는 방법
# assert 조건식
# assert 조건식, 에러메시지
x = int(input('3의 배수를 입력하세요: '))
assert x % 3 == 0, '3의 배수가 아닙니다.'    # 3의 배수가 아니면 예외 발생, 3의 배수이면 그냥 넘어감
print(x)