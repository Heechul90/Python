### Unit 22. 리스트와 튜플 응용하기
## 22.7 튜플 응용하기
## 22.7.1  튜플에서 특정 값의 인덱스 구하기
## index(값)은 튜플에서 특정 값의 인덱스를 구합니다.
a = (38, 21, 53, 62, 19, 53)
print(a.index(53))


## 22.7.2  특정 값의 개수 구하기
## count(값)은 튜플에서 특정 값의 개수를 구합니다.
a = (10, 20, 30, 15, 20, 40)
print(a.count(20))


## 22.7.3  for 반복문으로 요소 출력하기
a = (38, 21, 53, 62, 19)
for i in a:
    print(i, end = ' ')

print()


## 22.7.4  튜플 표현식 사용하기
## tuple(식 for 변수 in 리스트 if 조건식)
a = tuple(i for i in range(10) if i % 2 == 0)
print(a)


## 22.7.5  tuple에 map 사용하기
a = (1.2, 2.5, 3.7, 4.6)
a = tuple(map(int, a))
print(a)


## 22.7.6  튜플에서 가장 작은 수, 가장 큰 수, 합계 구하기
a = (38, 21, 53, 62, 19)
print(min(a))
print(max(a))
print(sum(a))