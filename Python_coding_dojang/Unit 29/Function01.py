### Unit 29. 함수 사용하기
## 29.1 Hello, world! 출력 함수 만들기
## def 함수이름():
##      코드

## 29.1.1  함수 만들기
def hello():
    print('Hello, world!')


## 29.1.2  함수 호출하기
## 함수()
hello()


## 29.1.3  소스 파일에서 함수를 만들고 호출하기

# function.py

# def hello():
#     print('Hello, world!')
# hello()


## 29.1.4  함수의 실행 순서
## 1) 파이썬 스크립트 최초 실행
## 2) hello 함수 호출
## 3) hello 함수 실행
## 4) print 함수 실행 및 'Hello, world!' 출력
## 5) hello 함수 종료
## 6) 파이썬 스크립트 종료


## 29.1.5  함수 작성과 함수 호출 순서
## 함수를 만들고 호출할 때 주의할 점이 있는데,
## 바로 함수를 만들기 전에 함수를 먼저 호출하면 안 된다는 점입니다
hello()                      # hello 함수를 만들기 전에 함수를 먼저 호출

def hello():                 # hello 함수를 만듦
    print('Hello, world!')


## 참고 | 빈 함수 만들기
def hello():
    pass