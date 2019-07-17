### Unit 17. while 반복문으로 Hello, world! 100번 출력하기
## 17.2 반복 횟수가 정해지지 않은 경우
## import 모듈
import random as rd    # random 모듈을 가져옴
print(rd.random())
print(rd.random())
print(rd.random())

## random.randint(a, b)
print(rd.randint(1, 6))
print(rd.randint(1, 6))
print(rd.randint(1, 6))


import random as rd        # random 모듈을 가져옴

i = 0
while i != 3:              # 3이 아닐 때 계속 반복
    i = rd.randint(1, 6)   # randint를 사용하여 1과 6 사이의 난수를 생성
    print(i)

# 참고 | random.choice
dice = [1, 2, 3, 4, 5, 6]
print(rd.choice(dice))
print(rd.choice(dice))
print(rd.choice(dice))