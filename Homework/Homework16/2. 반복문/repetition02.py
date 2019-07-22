### 반복문
## 문제 02
## (별 그리기)
## 5이상 9이하의 홀수를 입력받아 다이아몬드 형태의 별을 출력하는 프로그램을 작성하시오.
## 예) N=7
##    *
##   ***
##  *****
## *******
##  *****
##   ***
##    *

n = int(input('5이상 9이하의 홀수를 입력하시오.: '))


for i in range(1, n):
    for k in range(0, n - i -1):
        print(' ', sep = '', end = '')
    print('*' * (i * 2 - 1))

for i in reversed(range(1, n - 1)):
    for k in range(1, n - i):
        print(' ', sep = '', end = '')
    print('*' * (i * 2 - 1))
