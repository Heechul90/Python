### Unit 7. 출력 방법 알아보기
## 7.1 값을 여러 개 출력하기
print(1, 2, 3)
print('Hello', 'Python')


## 7.1.1 sep로 값 사이에 문자 넣기
# print(값1, 값2, sep='문자 또는 문자열')
# print(변수1, 변수2, sep='문자 또는 문자열')
print(1, 2, 3, sep = ', ')          # sep에 콤마와 공백을 지정
print(4, 5, 6, sep=',')             # sep에 콤마만 지정
print('Hello', 'Python', sep='')    # sep에 빈 문자열을 지정
print(1920, 1080, sep='x')          # sep에 x를 지정

