### Unit 25. 딕셔너리 응용하기
## 25.1 딕셔너리 조작하기

## 25.1.1  딕셔너리에 키-값 쌍 추가하기
## setdefault: 키-값 쌍 추가
## update: 키의 값 수정, 키가 없으면 키-값 쌍 추가

## 25.1.2  딕셔너리에 키와 기본값 저장하기
## setdefault(키)는 딕셔너리에 키-값 쌍을 추가합니다.
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.setdefault('e')
print(x)

## setdefault(키, 기본값)처럼 키와 기본값을 지정하면 값에 기본값을 저장한 뒤 해당 값을 반환합니다. 
x.setdefault('f', 100)
print(x)


## 25.1.3  딕셔너리에서 키의 값 수정하기
## update(키=값)은 이름 그대로 딕셔너리에서 키의 값을 수정합니다.
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.update(a=90)
print(x)

x.update(e=50)
print(x)

x.update(a=900, f=60)
print(x)

y = {1: 'one', 2: 'two'}
y.update({1: 'ONE', 3: 'THREE'})
print(y)

y.update([[2, 'TWO'], [4, 'FOUR']])
print(y)

y.update(zip([1, 2], ['one', 'two']))
print(y)

# 참고 | setdefault와 update의 차이
# setdefault는 키-값 쌍 추가만 할 수 있고, 이미 들어있는 키의 값은 수정할 수 없습니다. 
# update는 키-값 쌍 추가와 값 수정이 모두 가능합니다. 
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.setdefault('a', 90)
print(x)


## 25.1.4  딕셔너리에서 키-값 쌍 삭제하기
## pop(키)는 딕셔너리에서 특정 키-값 쌍을 삭제한 뒤 삭제한 값을 반환합니다.
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.pop('a')
print(x)

## pop(키, 기본값)처럼 기본값을 지정하면 딕셔너리에 키가 있을 때는 
## 해당 키-값 쌍을 삭제한 뒤 삭제한 값을 반환하지만 
## 키가 없을 때는 기본값만 반환합니다.
print(x.pop('z', 0))

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
del x['a']
print(x)


## 25.1.5  딕셔너리에서 임의의 키-값 쌍 삭제하기
## popitem()은 딕셔너리에서 임의의 키-값 쌍을 삭제한 뒤
## 삭제한 키-값 쌍을 튜플로 반환합니다.
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.popitem())
print(x)


## 25.1.6  딕셔너리의 모든 키-값 쌍을 삭제하기
## clear()는 딕셔너리의 모든 키-값 쌍을 삭제합니다.
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.clear()
print(x)


## 25.1.7  딕셔너리에서 키의 값을 가져오기
## get(키)는 딕셔너리에서 특정 키의 값을 가져옵니다.
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.get('a'))

## get(키, 기본값)처럼 기본값을 지정하면 
## 딕셔너리에 키가 있을 때는 해당 키의 값을 반환하지만 
## 키가 없을 때는 기본값을 반환합니다.
print(x.get('z', 0))


## 25.1.8  딕셔너리에서 키-값 쌍을 모두 가져오기
## items: 키-값 쌍을 모두 가져옴
## keys: 키를 모두 가져옴
## values: 값을 모두 가져옴
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.items())

print(x.keys())

print(x.values())


## 25.1.9  리스트와 튜플로 딕셔너리 만들기
## dict.fromkeys(키리스트)는 키 리스트로 딕셔너리를 생성하며 
## 값은 모두 None으로 저장합니다.
keys = ['a', 'b', 'c', 'd']
x = dict.fromkeys(keys)
print(x)

## dict.fromkeys(키리스트, 값)처럼 키 리스트와 값을 지정하면 
## 해당 값이 키의 값으로 저장됩니다.
y = dict.fromkeys(keys, 100)
print(y)

# 참고 | defaultdict 사용하기
# x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
# x['z']    # 키 'z'는 없음
# Traceback (most recent call last):
#   File "<pyshell#5>", line 1, in <module>
#     x['z']
# KeyError: 'z'

# defaultdict(기본값생성함수)
from collections import defaultdict  # collections 모듈에서 defaultdict를 가져옴
y = defaultdict(int)                 # int로 기본값 생성
print(y['z'])
print(int())

# 익명함수: lambda
def return_python():
    return 'python'

print(return_python())
y = defaultdict(return_python)
print(y['a'])
print(y[0])
print(y)