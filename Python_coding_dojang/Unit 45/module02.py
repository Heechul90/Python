### Unit 45. 모듈과 패키지 만들기
## 45.2 모듈과 시작점 알아보기

## 인터넷에 있는 파이썬 코드를 보다 보면
## if __name__ == '__main__':으로 시작하는 부분을 자주 만나게 됩니다.

# if __name__ == '__main__':
#     코드

# hello.py
# print('hello 모듈 시작')
# print('hello.py __name__:', __name__)    # __name__ 변수 출력
# print('hello 모듈 끝')

import hello  # hello 모듈을 가져옴

print('main.py __name__:', __name__)  # __name__ 변수 출력



## 45.2.1  스크립트 파일로 실행하거나 모듈로 사용하는 코드 만들기

# calc.py
# def add(a, b):
#     return a + b
#
# def mul(a, b):
#     return a * b
#
# if __name__ == '__main__':    # 프로그램의 시작점일 때만 아래 코드 실행
#     print(add(10, 20))
#     print(mul(10, 20))

import calc

calc.add(50, 60)
calc.mul(50, 60)