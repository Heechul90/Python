### Unit 17. while 반복문으로 Hello, world! 100번 출력하기
## 17.1 while 반복문 사용하기
## 초기식
## while 조건식:
##      반복할 코드
##      변화식

i = 0                          # 초기식
while i < 100:                 # while 조건식
     print('Hello, world!')    # 반복할 코드
     i += 1                    # 변화식



## 17.1.1  초깃값을 1부터 시작하기
i = 1
while i < 100:
    print('Hello, world!', i)
    i = i + 1



## 17.1.2  초깃값을 감소시키기
i = 100
while i > 0:
    print('Hello, world!', i)
    i = i - 1



## 17.1.3  입력한 횟수대로 반복하기
count = int(input('반복할 횟수를 입력하세요: '))

i = 0
while i < count:
    print('Hello, world!', i)
    i += 1

count = int(input('반복할 횟수를 입력하세요: '))

while count > 0:  # count가 0보다 클 때 반복
    print('Hello, world!', count)
    count -= 1   # count를 1씩 감소시킴