### Unit 38. 예외 처리 사용하기
## 38.4 예외 만들기
## 프로그래머가 직접 만든 예외를 사용자 정의 예외라고 합니다.

# class 예외이름(Exception):
#     def __init__(self):
#         super().__init__('에러메시지')

class NotThreeMultipleError(Exception):         # Exception을 상속받아서 새로운 예외를 만듦
    def __init__(self):
        super().__init__('3의 배수가 아닙니다.')


def three_multiple():
    try:
        x = int(input('3의 배수를 입력하세요: '))
        if x % 3 != 0:                         # x가 3의 배수가 아니면
            raise NotThreeMultipleError        # NotThreeMultipleError 예외를 발생시킴
        print(x)
    except Exception as e:
        print('예외가 발생했습니다.', e)


three_multiple()