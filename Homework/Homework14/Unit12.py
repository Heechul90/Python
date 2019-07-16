### Unit 12. 딕셔너리 사용하기
## 12.4 연습문제: 딕셔너리에 게임 캐릭터 능력치 저장하기
# 다음 소스 코드를 완성하여 
# 게임 캐릭터의 체력(health)과 이동 속도(movement speed)가 
# 출력되게 만드세요.
# 575.6
# 340
camille = {
    'health': 575.6,
    'health_regen': 1.7,
    'mana': 338.8,
    'mana_regen': 1.63,
    'melee': 125,
    'attack_damage': 60,
    'attack_speed': 0.625,
    'armor': 26,
    'magic_resistance': 32.1,
    'movement_speed': 340
}

print(camille['health'])
print(camille['movement_speed'])



### Unit 12. 딕셔너리 사용하기
# Unit 12.5 심사문제: 딕셔너리에 게임 캐릭터 능력치 저장하기

# alt+shift+e는 한줄씩 실행되어 다음과 같은 코드를 인식하지 못함.
# 따라서 코드 전체를 선택한 후 alt+shift+e를 실행하던지
# 파이썬 스크립트 전체를 실행해야 함. (전체를 실행해키는 단축키는 alt+shift+F10)

# 표준 입력으로 문자열 여러 개와 숫자(실수) 여러 개가 두 줄로 입력됩니다.
# 입력된 첫 번째 줄은 키, 두 번째 줄은 값으로 하여 딕셔너리를 생성한
# 뒤 딕셔너리를 출력하는 프로그램을 만드세요.
# input().split()의 결과를 변수 한 개에 저장하면 리스트로 저장됩니다.

x = input().split()
y = map(float, input().split())
print(dict(zip(x, y)))