### Unit 45. 모듈과 패키지 만들기
## 45.7 심사문제: 패키지 사용하기
## 표준 입력으로 정수가 입력됩니다.
## 주어진 calcpkg 패키지를 활용하여
## 입력된 정수의 제곱근과 입력된 정수를 반지름으로 하는 원의 넓이가 출력되게 만드세요.
## 제곱근은 calcpkg 패키지에서 operation 모듈의 squareroot 함수를 사용하고,
## 원의 넓이는 calcpkg 패키지에서 geometry 모듈의 circle_area 함수를 사용하세요
## (calcpkg 패키지를 사용하지 않고 계산하면 결과가 맞더라도 틀린 것으로 처리됩니다.
## 반드시 calcpkg 패키지를 사용하세요).


n = input('정수를 입력하시오.: ')

# 입력된 정수의 제곱근
import calcpkg1.operation

print(calcpkg1.operation.squareroot(int(n)))


# 입력된 정수를 반지름으로 하는 원의 넓이
import calcpkg1.geometry

print(calcpkg1.geometry.circle_area(int(n)))