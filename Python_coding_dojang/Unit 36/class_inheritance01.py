### Unit 36. 클래스 상속 사용하기
## 36.1 사람 클래스로 학생 클래스 만들기

# class 기반클래스이름:
#     코드
#
# class 파생클래스이름(기반클래스이름):
#     코드

class Person:
    def greeting(self):
        print('Hello')

class Student(Person):
    def study(self):
        print('Study hard!!!!')

james = Student()
james.greeting()       # 안녕하세요.: 기반 클래스 Person의 메서드 호출
james.study()          # 공부하기: 파생 클래스 Student에 추가한 study 메서드


# 참고 | 상속 관계 확인하기
# 클래스의 상속 관계를 확인하고 싶을 때는 issubclass 함수를 사용합니다.
# 즉, 클래스가 기반 클래스의 파생 클래스인지 확인합니다.
# 기반 클래스의 파생 클래스가 맞으면 True, 아니면 False를 반환합니다.

# issubclass(파생클래스, 기반클래스)
class Person:
    pass

class Student(Person):
    pass

issubclass(Student, Person)