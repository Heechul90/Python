### Unit 36. 클래스 상속 사용하기
## 36.3 기반 클래스의 속성 사용하기

class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕?'

class Student(Person):
    def __init__(self):
        print('Student __init__')
        self.school = '파이썬 코딩 도장이욤'

james = Student()
print(james.school)
print(james.hello)

# Person의 __init__ 메서드가 호출되지 않으면
# self.hello = '안녕하세요.'도 실행되지 않아서 속성이 만들어지지 않습니다.


## 36.3.1  super()로 기반 클래스 초기화하기
##  super()를 사용해서 기반 클래스의 __init__ 메서드를 호출해줍니다.
## 다음과 같이 super() 뒤에 .(점)을 붙여서 메서드를 호출하는 방식입니다.
## super().메서드()

class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세용'

class Student(Person):
    def __init__(self):
        print('Student __init__')
        super().__init__()         # super()로 기반 클래스의 __init__ 메서드 호출
        self.school = '파이썬 코딩 도장'

james = Student()
print(james.school)
print(james.hello)


## 36.3.2  기반 클래스를 초기화하지 않아도 되는 경우
## 만약 파생 클래스에서 __init__ 메서드를 생략한다면
## 기반 클래스의 __init__이 자동으로 호출되므로 super()는 사용하지 않아도 됩니다.

class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요'

class Student(Person):
    pass

james = Student()
print(james.hello)

# 이처럼 파생 클래스에 __init__ 메서드가 없다면
# 기반 클래스의 __init__이 자동으로 호출되므로 기반 클래스의 속성을 사용할 수 있습니다.


# 참고 | 좀 더 명확하게 super 사용하기
# super는 다음과 같이 파생 클래스와 self를 넣어서
# 현재 클래스가 어떤 클래스인지 명확하게 표시하는 방법도 있습니다.
# 물론 super()와 기능은 같습니다.
# uper(파생클래스, self).메서드

class Student(Person):
    def __init__(self):
        print('Student __init__')
        super(Student, self).__init__()     # super(파생클래스, self)로 기반 클래스의 메서드 호출
        self.school = '파이썬 코딩 도장'