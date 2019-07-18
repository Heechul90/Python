### Unit 23. 2차원 리스트 사용하기
## 23.4 2차원 리스트의 할당과 복사 알아보기
a = [[10, 20], [30, 40]]
b = a
print(b)
print(a)
b[0] [0] = 500
print(b)
print(a)

a = [[10, 20], [30, 40]]
b = a.copy()
b[0][0] = 500
print(b)
print(a)

a = [[10, 20], [30, 40]]
import copy             # copy 모듈을 가져옴
b = copy.deepcopy(a)    # copy.deepcopy 함수를 사용하여 깊은 복사
b[0][0] = 500
print(b)
print(a)