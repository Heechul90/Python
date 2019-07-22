### 조건문
## 문제 02
## 현재 상근이가 맞춰논 알람 시각을 입력으로 받아(시와 분)
## 원래 맞춰져 있는 알람을 45분 앞서는 시간으로 바꾸기
## 이를 구하는 프로그램을 작성하시오.

hour = int(input('시간을 입력하시오.: '))
min = int(input('분을 입력하시오.: '))

if min >= 45:
    min = min - 45
    print(hour,'시', min, '분')
else:
    hour = hour - 1
    min = min + 15
    print(hour, '시', min, '분')

