### Unit 12. 딕셔너리 사용하기
## 12.2 딕셔너리의 키에 접근하고 값 할당하기
## 딕셔너리[키]
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
print(lux['health'])

# 참고 | 딕셔너리에 키를 지정하지 않으면?
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
print(lux)    # 딕셔너리에 키를 지정하지 않으면 딕셔너리 전체를 뜻함


## 12.2.1  딕셔너리의 키에 값 할당하기
## 딕셔너리[키] = 값
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
lux['health'] = 2037    # 키 'health'의 값을 2037로 변경
lux['mana'] = 1184      # 키 'mana'의 값을 1184로 변경
print(lux)

lux['mana_regen'] = 3.28    # 키 'mana_regen'을 추가하고 값 3.28 할당
print(lux)

lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
# print(lux['attack_speed'])    # lux에는 'attack_speed' 키가 없음


## 12.2.2  딕셔너리에 키가 있는지 확인하기
## 키 in 딕셔너리
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
print('health' in lux)
print('attack_speed' in lux)

## 키 not in 딕셔너리
print('attack_speed' not in lux)
print('health' not in lux)

# 참고 | 해시


## 12.2.3  딕셔너리의 키 개수 구하기
## len(딕셔너리)
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
print(len(lux))
print(len({'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}))