### Unit 26. 세트 사용하기
## 26.6 세트 표현식 사용하기
## {식 for 변수 in 반복가능한객체}
## set(식 for 변수 in 반복가능한객체)
a = {i for i in 'apple'}
print(a)


## 26.6.1  세트 표현식에 if 조건문 사용하기
## {식 for 변수 in 세트 if 조건식}
## set(식 for 변수 in 세트 if 조건식)
a = {i for i in 'pineapple' if i not in 'apl'}
print(a)