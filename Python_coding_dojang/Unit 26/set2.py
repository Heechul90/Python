### Unit 26. 세트 사용하기
## 26.2 집합 연산 사용하기

## 합집합(union)
## 세트1 | 세트2
## set.union(세트1, 세트2)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)
print(set.union(a, b))


## 교집합(intersection)
## 세트1 & 세트2
## set.intersection(세트1, 세트2)
print(a & b)
print(set.intersection(a, b))


## 차집합(difference)
## 세트1 - 세트2
## set.difference(세트1, 세트2)
print(a - b)
print(set.difference(a, b))


## 대칭차집합(symmetric difference)
## 세트1 ^ 세트2
## set.symmetric_difference(세트1, 세트2)
print(a ^ b)
print(set.symmetric_difference(a, b))


## 26.2.1  집합 연산 후 할당 연산자 사용하기
## 세트1 |= 세트2
## 세트1.update(세트2)
a = {1, 2, 3, 4}
a |= {5}
print(a)

a = {1, 2, 3, 4}
a.update({5})
print(a)

## 세트1 &= 세트2
## 세트1.intersection_update(세트2)
a = {1, 2, 3, 4}
a &= {0, 1, 2, 3, 4}
print(a)

a = {1, 2, 3, 4}
a.intersection_update({0, 1, 2, 3, 4})
print(a)

## 세트1 ^= 세트2
## 세트1.symmetric_difference_update(세트2)
a = {1, 2, 3, 4}
a ^= {3, 4, 5, 6}
print(a)

a = {1, 2, 3, 4}
a.symmetric_difference_update({3, 4, 5, 6})
print(a)


## 26.2.2  부분 집합과 상위집합 확인하기
## 부분집합(subset)
## 현재세트 <= 다른세트
## 현재세트.issubset(다른세트)
a = {1, 2, 3, 4}
print(a <= {1, 2, 3, 4})
print(a.issubset({1, 2, 3, 4, 5}))

## 진부분집합(proper subset)
## 현재세트 < 다른세트
a = {1, 2, 3, 4}
print(a < {1, 2, 3, 4, 5})

## 상위집합(superset)
## 현재세트 >= 다른세트
## 현재세트.issuperset(다른세트)
a = {1, 2, 3, 4}
print(a >= {1, 2, 3, 4})
print(a.issuperset({1, 2, 3, 4}))

## 진상위집합(proper superset)
## 현재세트 > 다른세트
a = {1, 2, 3, 4}
print(a > {1, 2, 3})


## 26.2.3  세트가 같은지 다른지 확인하기
## 세트는 == 연산자를 사용하여 서로 같은지 확인할 수 있습니다.
a = {1, 2, 3, 4}
print(a == {1, 2, 3, 4})
print(a == {4, 2, 1, 3})

a = {1, 2, 3, 4}
print(a != {1, 2, 3})


## 26.2.4  세트가 겹치지 않는지 확인하기
## 현재세트.isdisjoint(다른세트)
a = {1, 2, 3, 4}
print(a.isdisjoint({5, 6, 7, 8}))       # 겹치는 요소가 없음
print(a.isdisjoint({3, 4, 5, 6}))       # a와 3, 4가 겹침