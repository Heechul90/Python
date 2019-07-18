### Unit 22. 리스트와 튜플 응용하기
## 22.5 리스트 표현식 사용하기
## [식 for 변수 in 리스트]
## list(식 for 변수 in 리스트)
a = [i for i in range(10)]        # 0부터 9까지 숫자를 생성하여 리스트 생성
print(a)

b = list(i for i in range(10))    # 0부터 9까지 숫자를 생성하여 리스트 생성
print(b)

c = [i + 5 for i in range(10)]    # 0부터 9까지 숫자를 생성하면서 값에 5를 더하여 리스트 생성
print(c)

d = [i * 2 for i in range(10)]    # 0부터 9까지 숫자를 생성하면서 값에 2를 곱하여 리스트 생성
print(d)

# 참고 | 대괄호와 list() 리스트 표현식
# 리스트 표현식은 [식 for 변수 in 리스트]처럼 [ ](대괄호)로 만들 수도 있고, 
# list(식 for 변수 in 리스트)처럼 list로 만들 수도 있습니다. 
# 둘 중에 성능은 대괄호 방식이 더 좋습니다.


## 22.5.1  리스트 표현식에서 if 조건문 사용하기
## [식 for 변수 in 리스트 if 조건식]
## list(식 for 변수 in 리스트 if 조건식)
a = [i for i in range(10) if i % 2 == 0]    # 0~9 숫자 중 2의 배수인 숫자(짝수)로 리스트 생성
print(a)

b = [i + 5 for i in range(10) if i % 2 == 1]    # 0~9 숫자 중 홀수에 5를 더하여 리스트 생성
print(b)


## 22.5.2  for 반복문과 if 조건문을 여러 번 사용하기
## [식 for 변수1 in 리스트1 if 조건식1     
##         for 변수2 in 리스트2 if 조건식2     
##              ...     
##              for 변수n in 리스트n if 조건식n]

## list(식 for 변수1 in 리스트1 if 조건식1         
##         for 변수2 in 리스트2 if 조건식2         
##              ...         
##              for 변수n in 리스트n if 조건식n)

a = [i * k for i in range(2, 10) for k in range(1, 10)]
print(a)

a = [i * j for j in range(2, 10)
           for i in range(1, 10)]
print(a)