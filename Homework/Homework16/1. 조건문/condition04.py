### 조건문
## 문제 03
## 세 자연수 a, b, c 가 피타고라스 정리 a2 + b2 = c2 를 만족하면 피타고라스 수라고 부른다.
## (여기서 a < b < c 이고 a + b > c)
## 예를 들면, 32 + 42 = 9 + 16 = 25 = 52 이므로 3, 4, 5는 피타고라스 수입니다.
## a + b + c = 1000 인 피타고라스 수를 구하시오. (답은 한가지 뿐이다.)

outerBreak = False
for a in range(1, 333):
    if outerBreak:
        break
    for b in range(a + 1, 500):
        c = 1000 -a -c
        if b >= c:
            continue
        if a**2 + b**2 == c**2:
            print(a, b, c, a + b + c)
            print(a**2, b**2, c**2)
            outerBreak = True
            break;