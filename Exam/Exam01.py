## 문제 3
## 두 개의 정수를 입력받아 작은 수에서부터 큰 수까지(큰 수 포함) 홀수의 합을
## 구해서 출력하는 프로그램을 for loop을 사용하여 작성하시오.

a, b = map(int, input('정수를 입력하시오.: ').split())


sum = 0
for i in range(a, b + 1):
    if i % 2 == 1:
        sum = sum + i

print(sum)



## 문제 4
## 연 복리 이자율을 입력받아(단위%) 원금이 2배가 되는데 최소 몇년이 걸리는지 알아보는
## 프로그램을 while loop을 사용하여 작성하시오.

rate = float(input('연 복리 이자율을 입력하시오.: '))
p = int(input('원금을 입력하시오.: '))
p   # 원금
p*2 # 원금 두배

interest = r_rate * p # 매년 이자


year = 0

while p < p*2:
    p = p + p*rate
    print(p)





## 문제 5
## bts 리스트가 주어졌을 때 아래와 같은 답이 나오도록 print문을 작성하시오.

bts = ['RM', '진', '슈가', '제이홉', '지민', '뷔', '정국']

# 1)
print(bts[-2])

# 2)
print(bts[0 : 1])

# 3)
print(bts[-2 : ])

# 4)
print(bts[2 : 5])

# 5)
print(bts[::2])



## 문제 6
## 다음과 같은 딕셔너리 vegetables가주어졌을 때 아래 그림과 같이
## 가격이 높은 것부터 내림차순으로 출력하는 프로그램을 작성하되,
## 가격은 길이를 7로 만들고 1000단위 쉼표를 찍은 뒤 우측정렬 하시오

vegetables = {'가지': 800, '오이': 600, '수박': 15000, '호박': 1000, '깻잎': 500}


result = []
for vegetable in vegetables.items():
    vegetable = list(vegetable)

    print(vegetable)


print(result)




## 문제 7

def isPalindrome(a):
    for i in range(len(a)//2):
        if a[i] != a[-1-i]:
            return False
    return True

maxNum = 0
for i in range(100, 1000):
    for k in range(i, 1000):
        if isPalindrome(str(i*k)):
            if i*k > maxNum:
                maxNum = i*k
                maxA = i
                maxB = k
print(maxNum, maxA, maxB)




## 문제 8

from pprint import pprint
import random

matrix = [[random.randint(1,4),random.randint(1,4),random.randint(1,4),random.randint(1,4),random.randint(1,4)],
           [random.randint(1,4),random.randint(1,4),random.randint(1,4),random.randint(1,4),random.randint(1,4)],
           [random.randint(1,4),random.randint(1,4),random.randint(1,4),random.randint(1,4),random.randint(1,4)],
           [random.randint(1,4),random.randint(1,4),random.randint(1,4),random.randint(1,4),random.randint(1,4)],
           [random.randint(1,4),random.randint(1,4),random.randint(1,4),random.randint(1,4),random.randint(1,4)]]

pprint(matrix, indent=4, width=20)
matrix[0][:]

def mines(i, k):
    if matrix[i][k] == matrix[i][k + 1] == matrix[i][k + 2]:
        return '*'
    if matrix[i][k] == matrix[i + 1][k] == matrix[i + 1][k]:
        return '*'



for i in range(5):
    for k in range(5):
        print(mines(i, k), end = '')
    print()



matrix = []
for i in range(row):
    matrix.append(list(input()))

matrix

## 문제 9
## 다음과 같은 리스트 a가 주어졌을 때 a의 각 원소를 제곱한 값을 원소로 갖는
## 리스트 b를 람다표현식을 사용하여 구하시오.
a = [1, 3, 5, 7, 9]

b = list(map(lambda x: x**x, a))

print(b)




