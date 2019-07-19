### Unit 25. 딕셔너리 응용하기
## 25.5 딕셔너리의 할당과 복사

x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
y = x

print(x)
print(y)

print(x == y)
print(x is y)

y['a'] = 99
print(x)
print(y)


x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
y = x.copy()

print(x)
print(y)

print(x == y)
print(x is y)

y['a'] = 99
print(x)
print(y)


## 25.5.1  중첩 딕셔너리의 할당과 복사 알아보기
x = {'a': {'python': '2.7'}, 'b': {'python': '3.6'}}
y = x.copy()

y['a']['python'] = '2.7.15'
print(x)
print(y)


x = {'a': {'python': '2.7'}, 'b': {'python': '3.6'}}
import copy             # copy 모듈을 가져옴
y = copy.deepcopy(x)    # copy.deepcopy 함수를 사용하여 깊은 복사
y['a']['python'] = '2.7.15'
print(x)
print(y)