### Unit 22. 리스트와 튜플 응용하기
## 22.2 리스트의 할당과 복사 알아보기

a = [0, 0, 0, 0, 0]
b = a
print(a)
print(b)
print(a is b)

b[2] = 99
print(a)
print(b)


a = [0, 0, 0, 0, 0]
b = a.copy()
print(a)
print(b)
print(a == b)
print(a is b)

b[2] = 99
print(a)
print(b)