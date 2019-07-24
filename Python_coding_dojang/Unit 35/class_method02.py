### Unit 35. 클래스 속성과 정적, 클래스 메서드 사용하기
## 35.2 35.3 클래스 메서드 사용하기
## 클래스 메서드는 다음과 같이 메서드 위에 @classmethod를 붙입니다.
## 이때 클래스 메서드는 첫 번째 매개변수에 cls를 지정해야 합니다(cls는 class에서 따왔습니다).

# class 클래스이름:
#     @classmethod
#     def 메서드(cls, 매개변수1, 매개변수2):
#         코드

class Person:
    count = 0 # 클래스 속성

    def __init__(self):
        Person.count = Person.count + 1                             # 인스턴스가 만들어질 때
                                                      # 클래스 속성 count에 1을 더함

    @classmethod
    def print_count(cls):
        print('{0}명 생성되었습니다'.format(cls.count))  # cls로 클래스 속성에 접근

james = Person()
maria = Person()
chul = Person()

Person.print_count()                                   # 2명 생성되었습니다.