### Unit 10. 리스트와 튜플 사용하기
## 10.1 리스트 만들기
## 리스트 = [값, 값, 값]

a = [38, 21, 53, 62, 19]
print(a)


## 10.1.1  리스트에 여러 가지 자료형 저장하기
person = ['james', 17, 175.3, True]
print(person)


## 10.1.2  빈 리스트 만들기
## 리스트 = []
## 리스트 = list()
a = []
print(a)
b = list()
print(b)


## 10.1.3  range를 사용하여 리스트 만들기
## range(횟수)
print(range(10))

## 리스트 = list(range(횟수))
b = list(range(5, 12))
print(b)

## 리스트 = list(range(시작, 끝, 증가폭))
c = list(range(-4, 10, 2))
print(c)

d = list(range(10, 0, -1))
print(d)