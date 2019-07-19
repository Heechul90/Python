### Unit 26. 세트 사용하기
## 26.9 심사문제: 공약수 구하기
## 표준 입력으로 양의 정수 두 개가 입력됩니다.
## 다음 소스 코드를 완성하여
## 두 숫자의 공약수를 세트 형태로 구하도록 만드세요.
## 단, 최종 결과는 공약수의 합으로 판단합니다.

# 입력
# 10 20
# 결과
# 18

# 입력
# 100 200
# 결과
# 217

x, y = map(int, input('문자열 두 개를 입력하세요: ').split())

a = []
for i in range(1, x + 1):
    if x % i == 0:
        a.append(i)
a = set(a)

b = []
for i in range(1, y + 1):
    if y % i == 0:
        b.append(i)
b = set(b)


divisor = a & b

result = 0
if type(divisor) == set:
    result = sum(divisor)

print(result)