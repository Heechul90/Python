### Unit 30. 함수에서 위치 인수와 키워드 인수 사용하기
## 30.4 매개변수에 초깃값 지정하기
## def 함수이름(매개변수=값):
##    코드

def personal_info(name, age, address = '비공개'):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

personal_info('홍길동', 30)

personal_info('이희철', 30, '대전시 유성구 궁동')


## 30.4.1  초깃값이 지정된 매개변수의 위치

# def personal_info(name, address='비공개', age):
#     print('이름: ', name)
#     print('나이: ', age)
#     print('주소: ', address)
#
#   File "<stdin>", line 1
# SyntaxError: non-default argument follows default argument

# 함수를 만들어보면 문법 에러가 발생합니다.
# 왜냐하면 함수를 이렇게 만들어버리면 personal_info('홍길동', 30)으로 함수를 호출했을 때
# 30이 어디로 들어가야 할지 알 수가 없기 때문입니다

# 즉, 다음과 같이 초깃값이 지정된 매개변수는 뒤쪽에 몰아주면 됩니다.
def personal_info(name, age, address='비공개'):
def personal_info(name, age=0, address='비공개'):
def personal_info(name='비공개', age=0, address='비공개'):