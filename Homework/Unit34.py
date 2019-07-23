### Unit 34. 클래스 사용하기
## 34.6 심사문제: 게임 캐릭터 클래스 만들기
## 표준 입력으로 게임 캐릭터 능력치(체력, 마나, AP)가 입력됩니다.
## 다음 소스 코드에서 애니(Annie) 클래스를 작성하여
## 티버(tibbers) 스킬의 피해량이 출력되게 만드세요.
## 티버의 피해량은 AP * 0.65 + 400이며
## AP(Ability Power, 주문력)는 마법 능력치를 뜻합니다.

# 입력
# 511.68 334.0 298

# 결과
# 티버: 피해량 593.7

# 입력
# 1803.68 1184.0 645

# 결과
# 티버: 피해량 819.25

class Annie:
    def __init__(self, health, mana, ability_power):
        self.health = health
        self.mana = mana
        self.ability_power = ability_power

    def tibbers(self):
        AP = ability_power
        print('티버: 피해량', AP * 0.65 + 400)

health, mana, ability_power = map(float, input().split())

x = Annie(health=health, mana=mana, ability_power=ability_power)
x.tibbers()

