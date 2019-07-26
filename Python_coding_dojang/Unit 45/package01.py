### Unit 45. 모듈과 패키지 만들기
## 45.3 패키지 만들기
## 모듈은 스크립트 파일이 한 개지만 패키지는 폴더(디렉터리)로 구성되어 있습니다.

# calcpkg/__init__.py
# # __init__.py 파일은 내용을 비워 둘 수 있음

## 폴더(디렉터리) 안에 __init__.py 파일이 있으면 해당 폴더는 패키지로 인식됩니다.
## 그리고 기본적으로 __init__.py 파일의 내용은 비워 둘 수 있습니다
## (파이썬 3.3 이상부터는 __init__.py 파일이 없어도 패키지로 인식됩니다.
## 하지만 하위 버전에도 호환되도록 __init__.py 파일을 작성하는 것을 권장합니다).


## 45.3.1  패키지에 모듈 만들기
## 첫 번째 모듈은 덧셈, 곱셈 함수가 들어있는 operation 모듈이고,
## 두 번째 모듈은 삼각형, 사각형의 넓이 계산 함수가 들어있는 geometry 모듈입니다

# calcpkg/operation.py
# def add(a, b):
#     return a + b
#
# def mul(a, b):
#     return a * b

# calcpkg/geometry.py
# def triangle_area(base, height):
#     return base * height / 2
#
# def rectangle_area(width, height):
#     return width * height


## 45.3.2  패키지 사용하기

# import 패키지.모듈
# 패키지.모듈.변수
# 패키지.모듈.함수()
# 패키지.모듈.클래스()

import calcpkg.operation                         # calcpkg 패키지의 operation 모듈을 가져옴
import calcpkg.geometry                          # calcpkg 패키지의 geometry 모듈을 가져옴

print(calcpkg.operation.add(10, 20))             # operation 모듈의 add 함수 사용
print(calcpkg.operation.mul(10, 20))             # operation 모듈의 mul 함수 사용

print(calcpkg.geometry.triangle_area(30, 40))    # geometry 모듈의 triangle_area 함수 사용
print(calcpkg.geometry.rectangle_area(30, 40))   # geometry 모듈의 rectangle_area 함수 사용



## 45.3.3  from import로 패키지의 모듈에서 변수, 함수, 클래스 가져오기
## 패키지의 모듈에서 from import로 함수(변수, 클래스)를 가져온 뒤
# 패키지와 모듈 이름을 붙이지 않고 사용할 수도 있습니다.

# from 패키지.모듈 import 변수
# from 패키지.모듈 import 함수
# from 패키지.모듈 import 클래스

from calcpkg.operation import add, mul
add(10, 20)
mul(10, 20)


# 참고 | 패키지의 모듈과 __name__
# 패키지의 모듈에서는 __name__ 변수에 패키지.모듈 형식으로 이름이 들어갑니다.
# 즉, calcpkg 패키지의 geometry.py에서 __name__의 값을 출력하도록 만들고,
# import로 가져오면 'calcpkg.geometry'가 나옵니다.

# 참고 | 모듈과 패키지를 찾는 경로
# 지금까지 모듈과 패키지는 현재 폴더(디렉터리)에 만들었습니다.
# 파이썬에서는 현재 폴더에 모듈, 패키지가 없으면 다음 경로에서 모듈, 패키지를 찾습니다.
import sys

sys.path