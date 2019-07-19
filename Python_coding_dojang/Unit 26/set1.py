### Unit 26. 세트 사용하기
## 26.1 세트 만들기
## 세트 = {값1, 값2, 값3}
fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
print(fruits)

fruits = {'orange', 'orange', 'cherry'}
print(fruits)

# 세트는 리스트, 튜플, 딕셔너리와는 달리 [ ](대괄호)로 특정 요소만 출력할 수는 없습니다.
# fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
# print(fruits[0])
# print(fruits['strawberry'])

# Traceback (most recent call last):
#   File "<pyshell#43>", line 1, in <module>
#     fruits['strawberry']
# TypeError: 'set' object is not subscriptable


## 26.1.1  세트에 특정 값이 있는지 확인하기
## 값 in 세트
fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
print('orange' in fruits)
print('peach' in fruits)

## 값 not in 세트
print('peach' not in fruits)
print('orange' not in fruits)


## 26.1.2  set를 사용하여 세트 만들기
## set(반복가능한객체)
a = set('apple')    # 유일한 문자만 세트로 만듦
print(a)

b = set(range(5))
print(b)

c = {}
print(type(c))
c = set()
print(type(c))
print(c)


# 참고 | 한글 문자열을 세트로 만들기
a = set('Hello')
print(a)

# 참고 | 세트 안에 세트 넣기
# 세트는 리스트, 딕셔너리와 달리 세트 안에 세트를 넣을 수 없습니다.
# a = {{1, 2}, {3, 4}}
# Traceback (most recent call last):
#   File "<pyshell#3>", line 1, in <module>
#     a = {{1, 2}, {3, 4}}
# TypeError: unhashable type: 'set'

# 참고 | 프로즌 세트
# 프로즌세트 = frozenset(반복가능한객체)
a = frozenset(range(10))
print(a)