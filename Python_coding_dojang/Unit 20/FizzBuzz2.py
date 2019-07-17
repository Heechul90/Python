### Unit 20. FizzBuzz 문제
## 20.2 3의 배수일 때와 5의 배수일 때 처리하기

for i in range(1, 101):
    if i % 3 == 0:
        print('Fizz', i)
    if i % 5 == 0:
        print('Buzz', i)




for i in range(1, 101):    # 1부터 100까지 100번 반복
    if i % 3 == 0:         # 3의 배수일 때
        print('Fizz')      # Fizz 출력
    elif i % 5 == 0:       # 5의 배수일 때
        print('Buzz')      # Buzz 출력
    else:
        print(i)           # 아무것도 해당되지 않을 때 숫자 출력        