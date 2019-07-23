### Unit 33. 클로저 사용하기
## 33.5 연습문제: 호출 횟수를 세는 함수 만들기
## 다음 소스 코드를 완성하여 함수 c를 호출할 때마다 호출 횟수가 출력되게 만드세요.
## 여기서는 함수를 클로저로 만들어야 합니다.

def counter():
    i = 0
    def count():
        nonlocal i
        i = i + 1
        return i
    return count

c = counter()
for i in range(10):
    print(c(), end=' ')