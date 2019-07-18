### Unit 22. 리스트와 튜플 응용하기
## 22.1 리스트 조작하기
## 먼저 리스트를 조작하는 메서드(method)입니다(메서드는 객체에 속한 함수를 뜻함

## 22.1.1  리스트에 요소 추가하기
## append: 요소 하나를 추가
## extend: 리스트를 연결하여 확장
## insert: 특정 인덱스에 요소 추가


## 22.1.2  리스트에 요소 하나 추가하기
## append(요소)는 리스트 끝에 요소 하나를 추가합니다. 
a = [10, 20, 30]
a.append(500)
print(a)
print(len(a))

a = []
a.append(10)
print(a)


## 22.1.3  리스트 안에 리스트 추가하기
a = [10, 20, 30]
a.append([500, 600])
print(a)
print(len(a))

# 약수 구해서 빈 리스트에 넣기
divisor = []
n = 60
for i in range(1, n + 1):
    if n % i == 0:
        divisor.append(i)

print(divisor)


## 22.1.4  리스트 확장하기
## extend(리스트)는 리스트 끝에 다른 리스트를 연결하여 리스트를 확장합니다.
a = [10, 20, 30]
a.extend([500, 600])
print(a)
print(len(a))


## 22.1.5  리스트의 특정 인덱스에 요소 추가하기
## insert(인덱스, 요소)는 리스트의 특정 인덱스에 요소 하나를 추가합니다. 
a = [10, 20, 30]
a.insert(2, 500)
print(a)
print(len(a))

# insert(0, 요소): 리스트의 맨 처음에 요소를 추가
a = [10, 20, 30]
a.insert(0, 500)
print(a)

# insert(len(리스트), 요소): 리스트 끝에 요소를 추가
a = [10, 20, 30]
a.insert(len(a), 500)
print(a)

a = [10, 20, 30]
a.insert(1, [500, 600])
print(a)

a = [10, 20, 30]
a[1:1] = [500, 600]
print(a)


## 22.1.6  리스트에서 요소 삭제하기
## pop: 마지막 요소 또는 특정 인덱스의 요소를 삭제
## remove: 특정 값을 찾아서 삭제


## 22.1.7  리스트에서 특정 인덱스의 요소를 삭제하기
## pop()은 리스트의 마지막 요소를 삭제한 뒤 삭제한 요소를 반환합니다.
a = [10, 20, 30]
a.pop()
print(a)

a = [10, 20, 30]
a.pop(1)
print(a)

a = [10, 20, 30]
del a[1]
print(a)


## 22.1.8  리스트에서 특정 값을 찾아서 삭제하기
## remove(값)은 리스트에서 특정 값을 찾아서 삭제합니다.
a = [10, 20, 30]
a.remove(20)
print(a)

a = [10, 20, 30, 20]
a.remove(20)
print(a)

# 참고 | 리스트로 스택과 큐 만들기
# deque(반복가능한객체)
from collections import deque    # collections 모듈에서 deque를 가져옴
a = deque([10, 20, 30])
print(a)
a.append(500)    # 덱의 오른쪽에 500 추가
print(a)
a.popleft()     # 덱의 왼쪽 요소 하나 삭제
print(a)


## 22.1.9  리스트에서 특정 값의 인덱스 구하기
## index(값)은 리스트에서 특정 값의 인덱스를 구합니다.
a = [10, 20, 30, 15, 20, 40]
print(a.index(20))


## 22.1.10 특정 값의 개수 구하기
## count(값)은 리스트에서 특정 값의 개수를 구합니다.
a = [10, 20, 30, 15, 20, 40]
print(a.count(20))


## 22.1.11 리스트의 순서를 뒤집기
## sort()는 리스트의 요소을 작은 순서대로 정렬합니다(오름차순).
## sort() 또는 sort(reverse=False): 리스트의 값을 작은 순서대로 정렬(오름차순)
## sort(reverse=True): 리스트의 값을 큰 순서대로 정렬(내림차순)
a = [10, 20, 30, 15, 20, 40]
a.sort()
print(a)
a.sort(reverse = True)
print(a)

# 참고 | sort 메서드와 sorted 함수
# sort는 메서드를 사용한 리스트를 변경하지만, 
# sorted 함수는 정렬된 새 리스트를 생성
a = [10, 20, 30, 15, 20, 40]
a.sort()            # a의 내용을 변경하여 정렬
print(a)

b = [10, 20, 30, 15, 20, 40]
print(sorted(b))    # 정렬된 새 리스트를 생성


## 22.1.13 리스트의 모든 요소를 삭제하기
## clear()는 리스트의 모든 요소를 삭제합니다.
a = [10, 20, 30]
a.clear()
print(a)

a = [10, 20, 30]
del a[:]
print(a)


## 22.1.14 리스트를 슬라이스로 조작하기
a = [10, 20, 30]
a[len(a):] = [500]
print(a)

a = [10, 20, 30]
a[len(a):] = [500, 600]
print(a)

# 참고 | 리스트가 비어 있는지 확인하기
# if not len(seq):    # 리스트가 비어 있으면 True
# if not len(seq):    # 리스트가 비어 있으면 True

# if not seq:         # 리스트가 비어 있으면 True    
# if seq:             # 리스트에 내용이 있으면 True

seq = [10, 20, 30]
print(seq[-1])

# a = []
# a[-1]               # 에러가 남

seq = []
if seq:               # 리스트에 요소가 있는지 확인
    print(seq[-1])    # 요소가 있을 때만 마지막 요소를 가져옴