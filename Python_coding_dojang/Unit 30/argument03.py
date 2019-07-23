### Unit 30. 함수에서 위치 인수와 키워드 인수 사용하기
## 30.3 키워드 인수와 딕셔너리 언패킹 사용하기
## 함수(**딕셔너리)

def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
personal_info(**x)

personal_info(**{'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'})


## 30.3.1  **를 두 번 사용하는 이유
## personal_info에 *x를 넣으면 x의 키가 출력됩니다.
## 즉, 딕셔너리를 한 번 언패킹하면 키를 사용한다는 뜻이 됩니다.
x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
personal_info(*x)

personal_info(**x)


## 30.3.2  키워드 인수를 사용하는 가변 인수 함수 만들기
## def 함수이름(**매개변수):
##    코드

def personal_info(**kwargs):
    for kw, arg in kwargs.items():
        print(kw, ':', arg, sep = '')

personal_info(name='홍길동')
personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')

# 딕셔너리 언패킹을 사용해도 됩니다.
# 다음과 같이 딕셔너리를 만들고 앞에 **를 붙여서 넣어봅니다.
x = {'name': '홍길동'}
personal_info(**x)

y = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동', 'job' : 'student'}
personal_info(**y)

# **kwargs를 사용한 가변 인수 함수는 다음과 같이
# 함수 안에서 특정 키가 있는지 확인한 뒤 해당 기능을 만듭니다.
def personal_info(**kwargs):
    if 'name' in kwargs:                    # in으로 딕셔너리 안에 특정 키가 있는지 확인
        print('이름: ', kwargs['name'])
    if 'age' in kwargs:
        print('나이: ', kwargs['age'])
    if 'address' in kwargs:
        print('주소: ', kwargs['address'])

# 참고 | 고정 인수와 가변 인수(키워드 인수)를 함께 사용하기
# 고정 인수와 가변 인수(키워드 인수)를 함께 사용할 때는
# 다음과 같이 고정 매개변수를 먼저 지정하고,
# 그 다음 매개변수에 **를 붙여주면 됩니다.
def personal_info(name, **kwargs):
    print(name)
    print(kwargs)

personal_info('이희철')
personal_info('이희철', age = 30, address = '대전시 유성구 궁동')
personal_info(**{'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'})

# 단, def personal_info(**kwargs, name):처럼
# **kwargs가 고정 매개변수보다 앞쪽에 오면 안 됩니다.
# 매개변수 순서에서 **kwargs는 반드시 가장 뒤쪽에 와야 합니다.


# 참고 | 위치 인수와 키워드 인수를 함께 사용하기
# 함수에서 위치 인수를 받는 *args와 키워드 인수를 받는 **kwargs를 함께 사용할 수도 있습니다
def custom_print(*args, **kwargs):
    print(*args, **kwargs)

custom_print(1, 2, 3, sep =':', end = '')
# 단, 이때 def custom_print(**kwargs, *args):처럼
# **kwargs가 *args보다 앞쪽에 오면 안 됩니다.
# 매개변수 순서에서 **kwargs는 반드시 가장 뒤쪽에 와야 합니다.