### 반복문
## 문제 03

## 디지털 시계에 하루동안(00:00~23:59) 3이 표시되는 시간을
## 초로 환산하면 총 몇 초(second) 일까요?
## 디지털 시계는 하루동안 다음과 같이 시:분(00:00~23:59)으로 표시됨.
## 00:00 (60초간 표시)
## 00:01
## …
## 23:59


second = 0
for i in range(0, 24):
    for k in range(0, 60):
        time = str(i) + str(k)
        if '3' in time:
            second = second + 60

print(second)
