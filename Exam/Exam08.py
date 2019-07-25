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
