### Unit 36. 클래스 상속 사용하기
## 36.2 상속 관계와 포함 관계 알아보기
## 36.2.1  상속 관계

class Person:
    def greeting(self):
        print('안녕하세요.')


class Student(Person):
    def study(self):
        print('공부하기')

# 상속은 명확하게 같은 종류이며 동등한 관계일 때 사용


## 36.2.2  포함 관계
class Person:
    def greeting(self):
        print('안녕하세요.')


class PersonList:
    def __init__(self):
        self.person_list = []            # 리스트 속성에 Person 인스턴스를 넣어서 관리

    def append_person(self, person):     # 리스트 속성에 Person 인스턴스를 추가하는 함수
        self.person_list.append(person)

# 상속을 사용하지 않고 속성에 인스턴스를 넣어서 관리하므로 PersonList가 Person을 포함하고 있습니다.
# 이러면 사람 목록 PersonList와 사람 Person은 동등한 관계가 아니라 포함 관계입니다.

# 같은 종류에 동등한 관계일 때는 상속을 사용하고,
# 그 이외에는 속성에 인스턴스를 넣는 포함 방식을 사용하면 됩니다.