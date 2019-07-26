### Unit 45. 모듈과 패키지 만들기
## 모듈(module)은 변수, 함수, 클래스 등을 모아 놓은 스크립트 파일이고,
## 패키지(package)는 여러 모듈을 묶은 것입니다.
## 모듈은 간단한 기능을 담을 때 사용하며,
## 패키지는 코드가 많고 복잡할 때 사용합니다.
## 즉, 패키지는 기능들이 모듈 여러 개로 잘게 나누어져 있고,
## 관련된 모듈끼리 폴더에 모여 있는 형태입니다.

## 45.1 모듈 만들기

#square2.py

# base = 2          # 변수
#
# def square(n):    # 함수
#     return base ** n


## 45.1.1  모듈 사용하기
## square2.py 파일과 main.py 파일은 반드시 같은 폴더에 있어야 합니다.

# import 모듈
# 모듈.변수
# 모듈.함수()

import square2  # import로 square2 모듈을 가져옴

print(square2.base)        # 모듈.변수 형식으로 모듈의 변수 사용
print(square2.square(10))  # 모듈.함수() 형식으로 모듈의 함수 사용


## 45.1.2  from import로 변수, 함수 가져오기
## 모듈에서 from import로 변수와 함수를 가져온 뒤 모듈 이름을 붙이지 않고 사용할 수도 있습니다.

# from 모듈 import 변수, 함수

from square2 import base, square
print(base)
square(10)



## 45.1.3  모듈에 클래스 작성하기

# person.py
# class Person:    # 클래스
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
#
#     def greeting(self):
#         print('안녕하세요. 저는 {0}입니다.'.format(self.name))

# import 모듈
# 모듈.클래스()

import person  # import로 person 모듈을 가져옴

# 모듈.클래스()로 person 모듈의 클래스 사용
maria = person.Person('마리아', 20, '서울시 서초구 반포동')
maria.greeting()



## 45.1.4  from import로 클래스 가져오기
## 모듈에서 from import로 클래스를 가져온 뒤 모듈 이름을 붙이지 않고 사용할 수도 있습니다.

# from 모듈 import 클래스

from person import Person
maria = Person('마리아', 20, '서울시 서초구 반포동')
maria.greeting()