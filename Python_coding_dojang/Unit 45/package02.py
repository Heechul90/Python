### Unit 45. 모듈과 패키지 만들기
## 45.4 패키지에서 from import 응용하기

## import calcpkg처럼 import 패키지 형식으로 패키지만 가져와서 모듈을 사용할 수는 없을까요?
## 이때는 calcpkg 패키지의 __init__.py 파일을 다음과 같이 수정합니다.

# from . import 모듈

# calcpkg/__init__.py
# from . import operation    # 현재 패키지에서 operation 모듈을 가져옴
# from . import geometry     # 현재 패키지에서 geometry 모듈을 가져옴

import calcpkg                                  # calcpkg 패키지만 가져옴

print(calcpkg.operation.add(10, 20))            # operation 모듈의 add 함수 사용
print(calcpkg.operation.mul(10, 20))            # operation 모듈의 mul 함수 사용

print(calcpkg.geometry.triangle_area(30, 40))   # geometry 모듈의 triangle_area 함수 사용
print(calcpkg.geometry.rectangle_area(30, 40))  # geometry 모듈의 rectangle_area 함수 사용


## 45.4.1  from import로 패키지에 속한 모든 변수, 함수, 클래스 가져오기
## 패키지에 속한 모든 변수, 함수, 클래스를 가져오려면 어떻게 해야 할까요?
## 먼저 main.py에서 import calcpkg를 from calcpkg import *와 같이 수정하고,
## 각 함수들도 앞에 붙은 calcpkg.operation, calcpkg.geometry를 삭제한 뒤 실행해봅니다.

# from 패키지 import *

from calcpkg import *          # calcpkg 패키지의 모든 변수, 함수, 클래스를 가져옴

print(add(10, 20))             # operation 모듈의 add 함수 사용
print(mul(10, 20))             # operation 모듈의 mul 함수 사용

print(triangle_area(30, 40))   # geometry 모듈의 triangle_area 함수 사용
print(rectangle_area(30, 40))  # geometry 모듈의 rectangle_area 함수 사용

dir()

## __init__.py에서 모듈 안의 함수를 가져오게 만들어야 합니다.
## 특히 현재 패키지(calcpkg)라는 것을 명확하게 나타내기 위해 모듈 앞에 .(점)을 붙입니다.

# from .모듈 import 변수, 함수, 클래스

# calcpkg/__init__.py
# # 현재 패키지의 operation, geometry 모듈에서 각 함수를 가져옴
# from .operation import add, mul
# from .geometry import triangle_area, rectangle_area


## 물론 __init__.py 파일에서 특정 함수(변수, 클래스)를 지정하지 않고
## *을 사용해서 모든 함수(변수, 클래스)를 가져와도 상관없습니다.

# from .모듈 import *

# calcpkg/__init__.py
# from .operation import *    # 현재 패키지의 operation 모듈에서 모든 변수, 함수, 클래스를 가져옴
# from .geometry import *     # 현재 패키지의 geometry 모듈에서 모든 변수, 함수, 클래스를 가져옴


## 패키지의 __init__.py에서
## from .모듈 import 변수, 함수, 클래스 또는 from .모듈 import * 형식으로 작성했다면
## 패키지를 가져오는 스크립트에서는 패키지.함수() 형식으로 사용할 수 있습니다
## (변수, 클래스도 같은 형식). 이때는 import calcpkg와 같이 패키지만 가져오면 됩니다.

# import 패키지
# 패키지.변수
# 패키지.함수()
# 패키지.클래스()

import calcpkg                         # calcpkg 패키지만 가져옴

print(calcpkg.add(10, 20))             # 패키지.함수 형식으로 operation 모듈의 add 함수 사용
print(calcpkg.mul(10, 20))             # 패키지.함수 형식으로 operation 모듈의 mul 함수 사용

print(calcpkg.triangle_area(30, 40))   # 패키지.함수 형식으로 geometry 모듈의 triangle_area 함수 사용
print(calcpkg.rectangle_area(30, 40))  # 패키지.함수 형식으로 geometry 모듈의 rectangle_area 함수 사용


# 참고 | __all__로 필요한 것만 공개하기
# 패키지의 __init__.py에서
# from .모듈 import *로 모든 변수, 함수, 클래스를 가져오면
# 패키지 외부에 공개하고 싶지 않은 것까지 공개하게 됩니다.
# 이때는 __all__에 공개할 모듈, 변수, 함수, 클래스를 리스트 형태로 지정해주면 됩니다.
# __all__이라는 이름 그대로 모든 것(*)을 가져갈 때의 목록을 정합니다.


from calcpkg import *          # calcpkg 패키지의 모든 변수, 함수, 클래스를 가져옴

print(add(10, 20))             # add 함수는 공개되어 있으므로 사용할 수 있음
print(mul(10, 20))             # 에러: mul 함수는 공개되어 있지 않으므로 사용할 수 없음

print(triangle_area(30, 40))   # triangle_area 함수는 공개되어 있으므로 사용할 수 있음
print(rectangle_area(30, 40))  # 에러: rectangle_area 함수는 공개되어 있으므로 사용할 수 있음


# 참고 | 하위 패키지 사용하기
# 패키지 안에 폴더(디렉터리)를 만들고 __init__.py와 모듈을 넣으면 하위 패키지가 됩니다.

# import 패키지.하위패키지.모듈

# calcpkg/__init__.py
# from .operation.element import *
# from .operation.logic import *
# from .geometry.shape import *
# from .geometry.vector import *
