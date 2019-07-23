### Unit 34. 클래스 사용하기
## 34.1 클래스와 메서드 만들기
## 래스는 class에 클래스 이름을 지정하고
##  :(콜론)을 붙인 뒤 다음 줄부터 def로 메서드를 작성하면 됩니다
# class 클래스이름:
#     def 메서드(self):
#         코드

class Person:
    def greeting(self):
        print('Hello')


# 인스턴스 = 클래스()
james = Person()


## 34.1.1  메서드 호출하기
## 인스턴스.메서드()
james.greeting()


## 34.1.2  파이썬에서 흔히 볼 수 있는 클래스
a = int(10)
a

b = list(range(10))
b

c = dict(x = 10, y = 20)
c

b = list(range(10))
b.append(20)
b

a = 10
type(a)

b = [0, 1, 2]
type(b)

c = {'x':10, 'y':20}
type(c)

maria = Person()
type(maria)


## 34.1.3  인스턴스와 객체의 차이점?
## 리스트 변수 a, b가 있으면 a, b는 객체입니다.
## 그리고 a와 b는 list 클래스의 인스턴스입니다.
a = list(range(10))
b = list(range(20))

# 참고 | 빈 클래스 만들기
class Person:
    pass


# 참고 | 메서드 안에서 메서드 호출하기
# 메서드 안에서 메서드를 호출할 때는 다음과 같이 self.메서드() 형식으로 호출해야 합니다.
class Person:

    def greeting(self):
        print('Hello')

    def hello(self):
        self.greeting()  # self.메서드() 형식으로 클래스 안의 메서드를 호출


james = Person()
james.hello()            # Hello


# 참고 | 특정 클래스의 인스턴스인지 확인하기
# 현재 인스턴스가 특정 클래스의 인스턴스인지 확인할 때는 isinstance 함수를 사용합니다.
# isinstance(인스턴스, 클래스)
class Person:
    pass

james = Person()
isinstance(james, Person)



def factorial(n):
    if not isinstance(n, int) or n < 0:    # n이 정수가 아니거나 음수이면 함수를 끝냄
        return None
    if n == 1:
        return 1
    return n * factorial(n - 1)