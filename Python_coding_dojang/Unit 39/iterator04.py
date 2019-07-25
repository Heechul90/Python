### Unit 39. 이터레이터 사용하기
## 39.4 iter, next 함수 활용하기
it = iter(range(3))
next(it)
next(it)
next(it)


## 39.4.1  iter
## iter(호출가능한객체, 반복을끝낼값)

import random
it = iter(lambda : random.randint(0, 5), 2)
next(it)
next(it)
next(it)


import random

for i in iter(lambda : random.randint(0, 5), 2):
    print(i, end=' ')

# 이렇게 iter 함수를 활용하면 if 조건문으로
# 매번 숫자가 2인지 검사하지 않아도 되므로 코드가 좀 더 간단해집니다.
import random

while True:
    i = random.randint(0, 5)
    if i == 2:
        break
    print(i, end=' ')


## 39.4.2  next
## next는 기본값을 지정할 수 있습니다.
## 기본값을 지정하면 반복이 끝나더라도 StopIteration이 발생하지 않고 기본값을 출력

# next(반복가능한객체, 기본값)
it = iter(range(3))
next(it, 10)