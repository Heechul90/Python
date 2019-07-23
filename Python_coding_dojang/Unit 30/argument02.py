### Unit 30. 함수에서 위치 인수와 키워드 인수 사용하기
## 30.2 키워드 인수 사용하기

def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

personal_info('이희철', 30, '대전시 유성구 궁동')

# 함수(키워드=값)
personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')
personal_info(age=30, address='서울시 용산구 이촌동', name='홍길동')

print(10, 20, 30, sep = '', end = '')