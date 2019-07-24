### Unit 37. 두 점 사이의 거리 구하기
## 37.1 두 점 사이의 거리 구하기

## 37.1.1  클래스로 점 구현하기
## 2차원 평면에서 위치를 표현하려면 x와 y값이 필요하겠죠?
## 다음과 같이 Point2D 클래스를 구현하고 x와 y를 속성으로 넣습니다.
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point2D(x = 30, y = 20)             # 점1
p2 = Point2D(x = 60, y = 50)             # 점2

print('p1 : {} {}'.format(p1.x, p1.y))   # 30 20
print('p2 : {} {}'.format(p2.x, p2.y))   # 60 50
