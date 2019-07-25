## 문제 3
## 두 개의 정수를 입력받아 작은 수에서부터 큰 수까지(큰 수 포함) 홀수의 합을
## 구해서 출력하는 프로그램을 for loop을 사용하여 작성하시오.

a, b = map(int, input('정수를 입력하시오.: ').split())


sum = 0
for i in range(a, b + 1):
    if i % 2 == 1:
        sum = sum + i

print(sum)






