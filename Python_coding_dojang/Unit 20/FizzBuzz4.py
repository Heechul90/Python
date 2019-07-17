### Unit 20. FizzBuzz 문제
## 20.4 논리 연산자를 사용하지 않고 3과 5의 공배수 처리하기

for i in range(1, 101):
    if i % 15 == 0:
        print('FizzBuzz',i)
    elif i % 3 == 0:
        print('Fizz', i)
    elif i % 5 == 0:
        print('Buzz', i)
    else:
        print(i)




for i in range(1, 101):      # 1부터 100까지 100번 반복
    if i % 15 == 0:          # 15의 배수(3과 5의 공배수)일 때
        print('FizzBuzz')    # FizzBuzz 출력
    elif i % 3 == 0:         # 3의 배수일 때
        print('Fizz')        # Fizz 출력
    elif i % 5 == 0:         # 5의 배수일 때
        print('Buzz')        # Buzz 출력
    else:
        print(i)             # 아무것도 해당되지 않을 때 숫자 출력