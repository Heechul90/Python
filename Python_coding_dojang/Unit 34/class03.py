### Unit 34. 클래스 사용하기
## 34.3 비공개 속성 사용하기

class Person:
    def __init__(self, name, age, address):
        self.hello = '안녕하니?'
        self.name = name
        self.age = age
        self.address = address

maria = Person('희철', 99, '독도')
maria.name

# class 클래스이름:
#     def __init__(self, 매개변수)
#         self.__속성 = 값


class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet  # 변수 앞에 __를 붙여서 비공개 속성으로 만듦


maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
maria.__wallet -= 10000         # 클래스 바깥에서 비공개 속성에 접근하면 에러가 발생함


class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet   # 변수 앞에 __를 붙여서 비공개 속성으로 만듦

    def pay(self, amount):
        self.__wallet -= amount  # 비공개 속성은 클래스 안의 메서드에서만 접근할 수 있음
        print('이제 {0}원 남았네요.'.format(self.__wallet))


maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
maria.pay(3000)
maria.pay(2000)


# 참고 | 공개 속성과 비공개 속성
# 클래스 바깥에서 접근할 수 있는 속성을 공개 속성(public attribute)이라 부르고,
# 클래스 안에서만 접근할 수 있는 속성을 비공개 속성(private attribute)이라 부릅니다.


# 참고 | 비공개 메서드 사용하기
# 속성뿐만 아니라 메서드도 이름이 __(밑줄 두 개)로 시작하면 클래스 안에서만 호출할 수 있는 비공개 메서드가 됩니다.
class Person:
    def __greeting(self):
        print('Hello')

    def hello(self):
        self.__greeting()  # 클래스 안에서는 비공개 메서드를 호출할 수 있음


james = Person()
james.__greeting()         # 에러: 클래스 바깥에서는 비공개 메서드를 호출할 수 없음