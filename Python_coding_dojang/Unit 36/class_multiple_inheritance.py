### Unit 36. 클래스 상속 사용하기
## 36.5 다중 상속 사용하기

# class 기반클래스이름1:
#     코드
#
# class 기반클래스이름2:
#     코드
#
# class 파생클래스이름(기반클래스이름1, 기반클래스이름2):
#     코드

class Person:
    def greeting(self):
        print('안녕하세요.')

class University:
    def manage_credit(self):
        print('학점 관리')

class Undergraduate(Person, University):
    def study(self):
        print('공부하기')


james = Undergraduate()
james.greeting()         # 안녕하세요.: 기반 클래스 Person의 메서드 호출
james.manage_credit()    # 학점 관리: 기반 클래스 University의 메서드 호출
james.study()            # 공부하기: 파생 클래스 Undergraduate에 추가한 study 메서드



## 36.5.1  다이아몬드 상속
class A:
    def greeting(self):
        print('안녕하세요. A입니다.')


class B(A):
    def greeting(self):
        print('안녕하세요. B입니다.')


class C(A):
    def greeting(self):
        print('안녕하세요. C입니다.')


class D(B, C):
    pass


x = D()
x.greeting()  # 안녕하세요. B입니다.


## 36.5.2  메서드 탐색 순서 확인하기
## 많은 프로그래밍 언어들이 다이아몬드 상속에 대한 해결책을 제시하고 있는데 ]
## 파이썬에서는 메서드 탐색 순서(Method Resolution Order, MRO)를 따릅니다.
# 클래스 D에 메서드 mro를 사용해보면 메서드 탐색 순서가 나옵니다
# (클래스.__mro__ 형식도 같은 내용)
# 클래스.mro()
D.mro()

# 참고 | object 클래스
# 파이썬에서 object는 모든 클래스의 조상입니다.
# 그래서 int의 MRO를 출력해보면 int 자기 자신과 object가 출력됩니다.
int.mro()

# 괄호 안에 object를 넣은 것과 같습니다.
class X:
    pass

class X(object):
    pass