### Unit 25. 딕셔너리 응용하기
## 25.2 반복문으로 딕셔너리의 키-값 쌍을 모두 출력하기
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

for i in x:
    print(i, end = ' ')

print()

# for 키, 값 in 딕셔너리.items():
#      반복할 코드
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for key, value in x.items():
    print(key, value)


## 25.2.1  딕셔너리의 키만 출력하기
## items: 키-값 쌍을 모두 가져옴
## keys: 키를 모두 가져옴
## values: 값을 모두 가져옴
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for value in x.values():
    print(value)