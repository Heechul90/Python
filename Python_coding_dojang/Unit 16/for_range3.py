### Unit 16. for 반복문으로 Hello, world! 100번 출력하기
## 16.3 시퀀스 객체로 반복하기
a = [10, 20, 30, 40, 50]
for i in a:
    print(i)


fruits = ('apple', 'orange', 'grape')
for fruit in fruits:
    print(fruit)


for letter in 'python':
    print(letter)

# reversed(시퀀스객체)
for letter in reversed('Python'):
    print(letter)