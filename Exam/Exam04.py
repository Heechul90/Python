## 문제 4
## 연 복리 이자율을 입력받아(단위%) 원금이 2배가 되는데 최소 몇년이 걸리는지 알아보는
## 프로그램을 while loop을 사용하여 작성하시오.


rate = float(input('연 복리 이자율을 입력하시오.: '))
money = int(input('당신의 원금을 입력하시오.: '))

import copy

rate = rate / 100
year = 0
principal = copy.copy(money)

while True:
    principal = principal + principal * rate

    if principal >= money * 2:
        break

    year = year + 1

print('연 복리 이자율: ', round(rate*100, 4), '%', '기간: ', year, '년')