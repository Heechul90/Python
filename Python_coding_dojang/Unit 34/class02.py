### Unit 34. 클래스 사용하기
## 34.2 속성 사용하기
## 속성(attribute)을 만들 때는 __init__ 메서드 안에서 self.속성에 값을 할당합니다.
## class 클래스이름:
##     def __init__(self):
##         self.속성 = 값

class Person:
    def __init__(self):
        self.hello = '안녕하세요 님아'

    def greeting(self):
        print(self.hello)

james = Person()
james.greeting()


## 34.2.1  self의 의미
## self는 인스턴스 자기 자신을 의미합니다.
## 우리는 인스턴스가 생성될 때 self.hello = '안녕하세요.'처럼 자기 자신에 속성을 추가했습니다.
## 여기서 __init__의 매개변수 self에 들어가는 값은 Person()이라 할 수 있습니다.
## 그리고 self가 완성된 뒤 james에 할당됩니다.
## 이후 메서드를 호출하면 현재 인스턴스가 자동으로 매개변수 self에 들어옵니다.
## 그래서 greeting 메서드에서 print(self.hello)처럼 속성을 출력할 수 있었던 것입니다.


## 34.2.2  인스턴스를 만들 때 값 받기
# class 클래스이름:
#     def __init__(self, 매개변수1, 매개변수2):
#         self.속성1 = 매개변수1
#         self.속성2 = 매개변수2

class Person:
    def __init__(self, name, age, address):
        self.hello = '안녕하세요 님아'
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print('{0} 저는 {1} 입니다.'.format(self.hello, self.name))

maria = Person('마리아', 20, '독도')
maria.greeting()

print('이름:', maria.name)       # 마리아
print('나이:', maria.age)        # 20
print('주소:', maria.address)    # 독도


# 참고 | 클래스의 위치 인수, 키워드 인수
# 클래스로 인스턴스를 만들 때 위치 인수와 키워드 인수를 사용할 수 있습니다.
class Person:
    def __init__(self, *args):
        self.name = args[0]
        self.age = args[1]
        self.address = args[2]

maria = Person(*['마리아', 20, '서울시 서초구 반포동'])
maria.name
maria.age
maria.address


# 키워드 인수와 딕셔너리 언패킹을 사용하려면 다음과 같이 **kwargs를 사용하면 됩니다.
class Person:
    def __init__(self, **kwargs):    # 키워드 인수
        self.name = kwargs['name']
        self.age = kwargs['age']
        self.address = kwargs['address']

maria1 = Person(name='마리아', age=20, address='서울시 서초구 반포동')
maria2 = Person(**{'name': '마리아', 'age': 20, 'address': '서울시 서초구 반포동'})

maria1.name

