### Unit 18. break, continue로 반복문 제어하기
## 18.3 입력한 횟수대로 반복하기

count = int(input('반복할 횟수를 입력하세요: '))

i = 0
while True:            # 무한 루프
    print(i)
    i += 1
    if i == count:     # i가 입력받은 값과 같을 때
        break          # 반복문을 끝냄


## 18.3.1  입력한 숫자까지 홀수 출력하기
count = int(input('반복할 횟수를 입력하세요: '))

for i in range(count + 1):  # 0부터 증가하면서 count까지 반복(count + 1)
    if i % 2 == 0:          # i를 2로 나누었을 때 나머지가 0이면 짝수
        continue            # 아래 코드를 실행하지 않고 건너뜀
    print(i)

