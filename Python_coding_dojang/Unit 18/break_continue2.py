### Unit 18. break, continue로 반복문 제어하기
## 18.2.1  for에서 continue로 코드 실행 건너뛰기
for i in range(100):       # 0부터 99까지 증가하면서 100번 반복
    if i % 2 == 0:         # i를 2로 나누었을 때 나머지가 0면 짝수
        continue           # 아래 코드를 실행하지 않고 건너뜀
    print(i)



##  18.2.2  while 반복문에서 continue로 코드 실행 건너뛰기
i = 0
while i < 100:        # i가 100보다 작을 때 반복. 0부터 99까지 증가하면서 100번 반복
    i += 1            # i를 1씩 증가시킴
    if i % 2 == 0:    # i를 2로 나누었을 때 나머지가 0이면 짝수
        continue      # 아래 코드를 실행하지 않고 건너뜀
    print(i)


# 참고 | 반복문과 pass
for i in range(10):    # 10번 반복
    pass               # 아무 일도 하지 않음

while True:    # 무한 루프
    pass       # 아무 일도 하지 않음

    