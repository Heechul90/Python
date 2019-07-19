### Unit 26. 세트 사용하기
## 26.4 세트의 할당과 복사

a = {1, 2, 3, 4}
b = a
print(a)
print(b)

print(a == b)
print(a is b)

b.add(5)

print(a)
print(b)

print(a == b)
print(a is b)


a = {1, 2, 3, 4}
b = a.copy()

print(a)
print(b)

print(a == b)
print(a is b)

b.add(5)

print(a)
print(b)

print(a == b)
print(a is b)