### Unit 25. 딕셔너리 응용하기
## 25.3 딕셔너리 표현식 사용하기
## {키: 값 for 키, 값 in 딕셔너리}
## dict({키: 값 for 키, 값 in 딕셔너리})

## x = {key: value for key, value in dict.fromkeys(keys).items()}
keys = ['a', 'b', 'c', 'd']
x = {key: value for key, value in dict.fromkeys(keys).items()}
print(x)


y = {key: 0 for key in dict.fromkeys(['a', 'b', 'c', 'd']).keys()}              # 키만 가져옴
z = {value: 0 for value in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.values()}       # 값을 키로 사용
print(y)
print(z)
x = {value: key for key, value in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.items()} # 키-값 자리를 바꿈
print(x)


## 25.3.1  딕셔너리 표현식에서 if 조건문 사용하기
## dict_del_by_value_error.py 참고


## {키: 값 for 키, 값 in 딕셔너리 if 조건식}
## dict({키: 값 for 키, 값 in 딕셔너리 if 조건식})
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

x = {key: value for key, value in x.items() if value != 20}
print(x)