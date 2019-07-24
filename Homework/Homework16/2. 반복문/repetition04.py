### 반복문
## 문제 04

## 1~1000에서 각 숫자의 개수를 구하시오.
## 예로 10 ~ 15 까지의 각 숫자의 개수를 구해보자.
## 10 = 1, 0
## 11 = 1, 1
## 12 = 1, 2
## 13 = 1, 3
## 14 = 1, 4
## 15 = 1, 5
## 그러므로 이 경우의 답은 0:1개, 1:7개, 2:1개, 3:1개, 4:1개, 5:1개

a, b = map(int, input('1~1000사이의 두 정수를 입력(두번째숫자가 더 커야함): ').split())

counts = [0] * 10

for i in range(1, 10):
    counts[i] += 1
for i in range(10, 100):
    counts[i // 10] += 1
    counts[i % 10] += 1
for i in range(100, 1000):
    counts[i // 100] += 1
    counts[(i % 100) // 10] += 1
    counts[i % 10] += 1
for i in range(1000, 1001):
    counts[i // 1000] += 1
    counts[(i % 1000) // 100] += 1
    counts[(i % 100) // 10] += 1
    counts[i % 10] += 1

print(counts)