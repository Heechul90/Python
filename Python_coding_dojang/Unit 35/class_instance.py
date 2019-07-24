### Unit 35. 클래스 속성과 정적, 클래스 메서드 사용하기
## 35.1 클래스 속성과 인스턴스 속성 알아보기
## 속성에는 클래스 속성과 인스턴스 속성 두 가지 종류가 있습니다.
## __init__ 메서드에서 만들었던 속성은 인스턴스 속성입니다.

## 35.1.1  클래스 속성 사용하기
# class 클래스이름:
#     속성 = 값

class Person:
    bag = []

    def put_bag(self, stuff):
        self.bag.append(stuff)

james = Person()
james.put_bag('책')

maria = Person()
maria.put_bag('열쇠')

print(james.bag)
print(maria.bag)


# 클래스.속성
# 클래스 속성에 접근할 때는 다음과 같이 클래스 이름으로 접근하면 좀 더 코드가 명확해집니다.
class Person:
    bag = []

    def put_bag(self, stuff):
        Person.bag.append(stuff)  # 클래스 이름으로 클래스 속성에 접근

print(Person.bag)


# 참고 | 속성, 메서드 이름을 찾는 순서
# 파이썬에서는 속성, 메서드 이름을 찾을 때 인스턴스, 클래스 순으로 찾습니다


## 35.1.2  인스턴스 속성 사용하기
## 그럼 가방을 여러 사람이 공유하지 않으려면 어떻게 해야 할까요?

class Person:
    def __init__(self):
        self.bag = []

    def put_bag(self, stuff):
        self.bag.append(stuff)

james = Person()
james.put_bag('책')

maria = Person()
maria.put_bag('열쇠')

print(james.bag)
print(maria.bag)

# 클래스 속성과 인스턴스 속성의 차이점
# 클래스 속성: 모든 인스턴스가 공유. 인스턴스 전체가 사용해야 하는 값을 저장할 때 사용
# 인스턴스 속성: 인스턴스별로 독립되어 있음. 각 인스턴스가 값을 따로 저장해야 할 때 사용


## 35.1.3  비공개 클래스 속성 사용하기
## 클래스 속성을 만들 때 __속성과 같이 __(밑줄 두 개)로 시작하면 비공개 속성이 됩니다.

# class 클래스이름:
#     __속성 = 값    # 비공개 클래스 속성

class Knight:
    __item_limit = 10               # 비공개 클래스 속성

    def print_item_limit(self):
        print(Knight.__item_limit)  # 클래스 안에서만 접근할 수 있음

x = Knight()
x.print_item_limit()                # 10

print(Knight.__item_limit)          # 클래스 바깥에서는 접근할 수 없음

# 클래스 Knight의 비공개 클래스 속성 __item_limit는 클래스 안의 print_item_limit 메서드에서만 접근할 수 있고,
# 클래스 바깥에서 접근하면 에러가 발생
# 비공개 클래스 속성은 클래스 바깥으로 드러내고 싶지 않은 값에 사용


# 참고 | 클래스와 메서드의 독스트링 사용하기
# 함수와 마찬가지로 클래스와 메서드도 독스트링을 사용할 수 있습니다.
# 다음과 같이 클래스와 메서드를 만들 때 :(콜론) 바로 다음 줄에 """ """(큰따옴표 세 개)
# 또는 ''' '''(작은따옴표 세 개)로 문자열을 입력하면 됩니다.
# 클래스의 독스트링은 클래스.__doc__ 형식으로 사용하고,
# 메서드의 독스트링은 클래스.메서드.__doc__ 또는 인스턴스.메서드.__doc__ 형식으로 사용

class Person:
    '''사람 클래스입니다.'''

    def greeting(self):
        '''인사 메서드입니다.'''
        print('Hello')


print(Person.__doc__)           # 사람 클래스입니다.
print(Person.greeting.__doc__)  # 인사 메서드입니다.

maria = Person()
print(maria.greeting.__doc__)   # 인사 메서드입니다.
