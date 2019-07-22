### 반복문
## 문제 06
## 1부터 10까지 자연수를 각각 제곱해 더하면 다음과 같다. (제곱의 합).
# 1**2 + 2**2 + ... + 10**2 = 385
# 1부터 10을 먼저 더한 다음에 그 결과를 제곱하면 다음과 같습니다 (합의 제곱).
# (1 + 2 + ... + 10)**2 = 55**2 = 3025
# 따라서 1부터 10까지 자연수에 대해
# "합의 제곱"과 "제곱의 합"의 차이는 3025 - 385 = 2640 이 된다.
# 입력으로 자연수 N을 받아,
# 1부터 N까지 자연수에 대해 "합의 제곱"과 "제곱의 합"의 차이는 얼마인가?


n = int(input('정수를 입력하시오.: '))

square_sum = 0
sum_square = 0
for i in range(1, n + 1):
    square_sum = square_sum + i**2
    sum_square = sum_square + i
sum_square = sum_square**2

print('합의 제곱 :', sum_square)
print('제곱의 합 :', square_sum)
print('합의 제곱 - 제곱의 합 = ', sum_square - square_sum)