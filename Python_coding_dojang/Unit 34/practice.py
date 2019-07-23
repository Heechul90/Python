### Unit 34. 클래스 사용하기
## 34.5 연습문제: 게임 캐릭터 클래스 만들기
## 다음 소스 코드에서 클래스를 작성하여 게임 캐릭터의 능력치와 '베기'가 출력되게 만드세요.



class Knight:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    def slash(self):
        print('베기')





x = Knight(health=542.4, mana=210.3, armor=38)
print(x.health, x.mana, x.armor)
x.slash()