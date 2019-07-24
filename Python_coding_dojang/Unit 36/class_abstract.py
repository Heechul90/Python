### Unit 36. 클래스 상속 사용하기
## 36.6 추상 클래스 사용하기
## 파이썬은 추상 클래스(abstract class)라는 기능을 제공합니다.
## 추상 클래스는 메서드의 목록만 가진 클래스이며 상속받는 클래스에서 메서드 구현을 강제하기 위해 사용합니다.

# from abc import *
#
# class 추상클래스이름(metaclass=ABCMeta):
#     @abstractmethod
#     def 메서드이름(self):
#         코드

from abc import *
class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def go_to_school(selfs):
        pass

class Student(StudentBase):
    def study(self):
        print('공부하기')

james = Student()
james.study()

# 추상 클래스를 상속받았다면 @abstractmethod가 붙은 추상 메서드를 모두 구현해야 합니다.


from abc import *


class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def go_to_school(self):
        pass


class Student(StudentBase):
    def study(self):
        print('공부하기')

    def go_to_school(self):
        print('학교가기')


james = Student()
james.study()
james.go_to_school()



## 36.6.1  추상 메서드를 빈 메서드로 만드는 이유
## 추상 클래스는 인스턴스로 만들 수가 없다는 점입니다.
james = StudentBase()

# @abstractmethod
#     def study(self):
#         pass    # 추상 메서드는 호출할 일이 없으므로 빈 메서드로 만듦
#
#     @abstractmethod
#     def go_to_school(self):
#         pass    # 추상 메서드는 호출할 일이 없으므로 빈 메서드로 만듦

# 추상 클래스는 인스턴스로 만들 때는 사용하지 않으며 오로지 상속에만 사용
# 파생 클래스에서 반드시 구현해야 할 메서드를 정해 줄 때 사용