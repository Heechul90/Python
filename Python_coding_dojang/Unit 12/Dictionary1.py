### Unit 12. 딕셔너리 사용하기
## 12.1 딕셔너리 만들기
## 딕셔너리 = {키1: 값1, 키2: 값2}
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
print(lux)


## 12.1.1  키 이름이 중복되면?
lux = {'health': 490, 'health': 800, 'mana': 334, 'melee': 550, 'armor': 18.72}
print(lux['health'])    # 키가 중복되면 가장 뒤에 있는 값만 사용함
print(lux)


## 12.1.2  딕셔너리 키의 자료형
x = {100: 'hundred', False: 0, 3.5: [3.5, 3.5]}
print(x)


## 12.1.3  빈 딕셔너리 만들기
## 딕셔너리 = {}
## 딕셔너리 = dict()
x = {}
print(x)
y = dict()
print(y)


## 12.1.4  dict로 딕셔너리 만들기
## 딕셔너리 = dict(키1=값1, 키2=값2)
## 딕셔너리 = dict(zip([키1, 키2], [값1, 값2]))
## 딕셔너리 = dict([(키1, 값1), (키2, 값2)])
## 딕셔너리 = dict({키1: 값1, 키2: 값2})
lux1 = dict(health=490, mana=334, melee=550, armor=18.72)                         # 키=값 형식으로 딕셔너리를 만듦
print(lux1)

lux2 = dict(zip(['health', 'mana', 'melee', 'armor'], [490, 334, 550, 18.72]))    # zip 함수로
print(lux2)                                                                       # 키 리스트와 값 리스트를 묶음

lux3 = dict([('health', 490), ('mana', 334), ('melee', 550), ('armor', 18.72)])
print(lux3)                                                                       # (키, 값) 형식의 튜플로 딕셔너리를 만듦

lux4 = dict({'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72})           # dict 안에서
lux4                                                                              # 중괄호로 딕셔너리를 만듦

