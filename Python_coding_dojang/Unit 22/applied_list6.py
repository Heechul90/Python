### Unit 22. 리스트와 튜플 응용하기
## 22.6 리스트에 map 사용하기
## list(map(함수, 리스트))
## tuple(map(함수, 튜플))

a = [1.2, 2.5, 3.7, 4.6]
for i in range(len(a)):
    a[i] = int(a[i])

print(a)

a = list(map(str, range(10)))
print(a)


## 22.6.1  input().split()과 map

a = input().split()
print(a)

a = map(int, input().split())
print(a)
print(list(a))


x = input().split()    # input().split()의 결과는 문자열 리스트
m = map(int, x)        # 리스트의 요소를 int로 변환, 결과는 맵 객체
a, b = m               # 맵 객체는 변수 여러 개에 저장할 수 있음
