### Unit 18. break, continue로 반복문 제어하기
## 18.1 break로 반복문 끝내기
## 18.1.1  while에서 break로 반복문 끝내기
i = 0
while True:         # 무한 루프
    print(i)
    i += 1          # i를 1씩 증가시킴
    if i == 30:     # i가 30일 때
        break       # 반복문을 끝냄. while의 제어흐름을 벗어남



## 18.1.2  for에서 break로 반복문 끝내기
for i in range(10000):    # 0부터 9999까지 반복
    print(i)
    if i == 30:           # i가 30일 때
        break             # 반복문을 끝냄. for의 제어흐름을 벗어남