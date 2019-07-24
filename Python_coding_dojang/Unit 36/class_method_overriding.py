### Unit 36. 클래스 상속 사용하기
## 36.4 메서드 오버라이딩 사용하기

class Person:
    def greeting(self):
        print('안녕하세요.')


class Student(Person):
    def greeting(self):
        print('안녕하세요. 저는 파이썬 코딩 도장 학생입니다.')


james = Student()
james.greeting()

# Person 클래스의 greeting 메서드를 무시하고 Student 클래스에서 새로운 greeting 메서드를 만들었습니다.
# 프로그램에서 어떤 기능이 같은 메서드 이름으로 계속 사용되어야 할 때 메서드 오버라이딩을 활용

class Person:
    def greeting(self):
        print('안녕하세요.')


class Student(Person):
    def greeting(self):
        super().greeting()                    # 기반 클래스의 메서드 호출하여 중복을 줄임
        print('저는 파이썬 코딩 도장 학생입니다.')


james = Student()
james.greeting()

# 메서드 오버라이딩은 원래 기능을 유지하면서 새로운 기능을 덧붙일 때 사용합니다.