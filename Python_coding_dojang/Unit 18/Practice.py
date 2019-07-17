### Unit 18. break, continue로 반복문 제어하기
## 18.5 연습문제: 3으로 끝나는 숫자만 출력하기
## 다음 소스 코드를 완성하여 0과 73 사이의 숫자 중 
## 3으로 끝나는 숫자만 출력되게 만드세요.
## 3 13 23 33 43 53 63 73
i = 0
while True:
    if i % 10 != 3:
        i = i + 1
        continue
    if i > 73:
        break
    print(i, end = ' ')
    i = i + 1

print()

i = 0
while True:
    i = i + 1
    if i % 10 == 3:
        print(i)
    if i == 73:
        break