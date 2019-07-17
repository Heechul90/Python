### Unit 16. for 반복문으로 Hello, world! 100번 출력하기
## 16.2 for와 range 응용하기
## 16.2.1  시작하는 숫자와 끝나는 숫자 지정하기

for i in range(5, 12):          # 5부터 11까지 반복
    print('Hello, world!', i)



## 16.2.2  증가폭 사용하기
for i in range(1, 10, 2):       # 0부터 8까지 2씩 증가
    print('Hello, world!', i)



## 16.2.3  숫자를 감소시키기
for i in range(10, 0):          # range(10, 0)은 동작하지 않음
    print('Hello, world!', i)

for i in range(10, 0, -1):      # 10에서 1까지 1씩 감소
    print('Hello, world!', i)

# for 변수 in reversed(range(횟수))
# for 변수 in reversed(range(시작, 끝))
# for 변수 in reversed(range(시작, 끝, 증가폭))
for i in reversed(range(10)):   # range에 reversed를 사용하여 숫자의 순서를 반대로 뒤집음
    print('Hello, world!', i)    # 9부터 0까지 10번 반복

# 참고 | 반복문의 변수 i를 변경할 수 있을까?
for i in range(10):
    print(i, end = ' ')
    i = 10


## 16.2.4  입력한 횟수대로 반복하기
count = int(input('반복할 횟수를 입력하세요: '))

for i in range(count):
    print('Hello, world!', i)