### Unit 11. 시퀀스 자료형 활용하기
## 11.2 시퀀스 객체의 요소 개수 구하기
## 11.2.1  리스트와 튜플의 요소 개수 구하기
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(len(a))

b = (38, 76, 43, 62, 19)
print(len(b))


## 11.2.2  range의 숫자 생성 개수 구하기
print(len(range(0, 10, 2)))


## 11.2.3  문자열의 길이 구하기
hello = 'Hello, world!'
print(len(hello))

hello = '안녕하세요'
print(len(hello))

# 참고 | UTF-8 문자열의 바이트 수 구하기
hello = '안녕하세요'
print(len(hello.encode('utf-8')))