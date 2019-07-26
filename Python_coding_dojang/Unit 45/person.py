### Unit 45. 모듈과 패키지 만들기
## 45.1.3  모듈에 클래스 작성하기

# person.py


class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print('안녕하세요. 저는 {0}입니다'.format(self.name))