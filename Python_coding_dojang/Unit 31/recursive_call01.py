### Unit 31. 함수에서 재귀호출 사용하기
## 31.1 재귀호출 사용하기

def hello():
    print('Hello, world')
    hello()

hello()


## 31.1.1  재귀호출에 종료 조건 만들기
## 재귀호출을 사용하려면 반드시 다음과 같이 종료 조건을 만들어주어야 합니다.
def hello(count):
    if count == 0:                  # 종료 조건을 만듦. count가 0이면 다시 hello 함수를 호출하지 않고 끝냄
        return

    print('Hello, world!', count)

    count -= 1                     # count를 1 감소시킨 뒤
    hello(count)                   # 다시 hello에 넣음


hello(5)  # hello 함수 호출