### Unit 19. 계단식으로 별 출력하기
for i in range(6):
    print('*' * i)


## 19.1 중첩 루프 사용하기

for i in range(5):                      # 5번 반복. 바깥쪽 루프는 세로 방향
    for j in range(5):                  # 5번 반복. 안쪽 루프는 가로 방향
        print('j:', j, sep='', end=' ') # j값 출력. end에 ' '를 지정하여 줄바꿈 대신 한 칸 띄움
    print('i:', i, '\\n', sep='')       # i값 출력, 개행 문자 모양도 출력
                                        # 가로 방향으로 숫자를 모두 출력한 뒤 다음 줄로 넘어감
                                        # (print는 기본적으로 출력 후 다음 줄로 넘어감)


for i in range(6):
    print('*' * i)
