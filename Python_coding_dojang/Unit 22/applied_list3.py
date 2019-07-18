### Unit 22. 리스트와 튜플 응용하기
## 22.3 반복문으로 리스트의 요소를 모두 출력하기

## 22.3.1  for 반복문으로 요소 출력하기
## for 변수 in 리스트:
##      반복할 코드
a = [38, 21, 53, 62, 19]
for i in a:
    print(i)

for i in [38, 21, 53, 62, 19]:
    print(i)


## 22.3.2  인덱스와 요소를 함께 출력하기
## for 인덱스, 요소 in enumerate(리스트):
a = [38, 21, 53, 62, 19]
for index, value in enumerate(a):
    print(index, value)

for index, value in enumerate(a):
    print(index + 1, value)

## for 인덱스, 요소 in enumerate(리스트, start=숫자):
for index, value in enumerate(a, start = 1):
    print(index, value)

# 참고 | for 반복문에서 인덱스로 요소를 출력하기
a = [38, 21, 53, 62, 19]
for i in range(len(a)):
    print(a[i])


## 22.3.3  while반복문으로 요소 출력하기
a = [38, 21, 53, 62, 19]
while i < len(a):
    print(a[i])
    i += 1

# 인덱스는 0부터 4, len(a)는 5
# 같게 하면 에러난다
# while i <= len(a):
#     print(a[i])
#     i += 1