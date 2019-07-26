### Unit 44. 모듈과 패키지 사용하기
## 모듈(module)은 각종 변수, 함수, 클래스를 담고 있는 파일이고,
## 패키지(package)는 여러 모듈을 묶은 것입니다.

# 참고 | 모듈, 패키지, 라이브러리
# 모듈: 특정 기능을 .py 파일 단위로 작성한 것입니다.
# 키지: 특정 기능과 관련된 여러 모듈을 묶은 것입니다.
#      패키지는 모듈에 네임스페이스(namespace, 이름공간)를 제공합니다
# 파이썬 표준 라이브러리: 파이썬에 기본으로 설치된 모듈과 패키지, 내장 함수를 묶어서
#                     파이썬 표준 라이브러리(Python Standard Library, PSL)라 부릅니다.


## 44.1 import로 모듈 가져오기
## 모듈은 import 키워드로 가져올 수 있습니다(모듈을 여러 개 가져올 때는 모듈을 콤마로 구분).

# import 모듈
# import 모듈1, 모듈2
# 모듈.변수
# 모듈.함수()
# 모듈.클래스()

import math
math.pi

# math 모듈의 제곱근 함수 sqrt를 사용해보겠습니다.

math.sqrt(4)
math.sqrt(2)


## 44.1.1  import as로 모듈 이름 지정하기
## 모듈의 함수를 사용할 때 math.sqrt처럼 일일이 math를 입력하기 귀찮은 사람도 있겠죠?
## 이때는 import as를 사용하여 모듈의 이름을 지정할 수 있습니다.

# import 모듈 as 이름

import math as m    # math 모듈을 가져오면서 이름을 m으로 지정
m.sqrt(4.0)         # m으로 제곱근 함수 사용
m.sqrt(2.0)         # m으로 제곱근 함수 사용


## 44.1.2  from import로 모듈의 일부만 가져오기
## import as로 모듈의 이름을 지정하는 방법보다 좀 더 편한 방법이 있습니다.
## 이번에는 from import로 원하는 변수만 가져와보겠습니다.

# from 모듈 import 변수

from math import pi    # math 모듈에서 변수 pi만 가져옴
pi                     # pi를 바로 사용하여 원주율 출력


## 모듈의 변수를 가져왔으니 이번에는 함수를 가져와보겠습니다(물론 클래스도 가져올 수 있습니다).

# from 모듈 import 함수
# from 모듈 import 클래스

from math import sqrt    # math 모듈에서 sqrt 함수만 가져옴
sqrt(4.0)                # sqrt 함수를 바로 사용
sqrt(2.0)                # sqrt 함수를 바로 사용


## 하지만 math 모듈에서 가져올 변수와 함수가 여러 개일 수도 있겠죠?
## 이때는 import 뒤에 가져올 변수, 함수, 클래스를 콤마로 구분하여 여러 개를 지정해주면 됩니다.

# from 모듈 import 변수, 함수, 클래스

from math import pi, sqrt    # math 모듈에서 pi, sqrt를 가져옴
pi                           # pi로 원주율 출력
sqrt(4.0)                    # sqrt 함수 사용
sqrt(2.0)                    # sqrt 함수 사용


## from import는 모듈의 모든 변수, 함수, 클래스를 가져오는 기능도 있습니다.

# from 모듈 import *

from math import *    # math 모듈의 모든 변수, 함수, 클래스를 가져옴
pi                    # pi로 원주율 출력
sqrt(4.0)             # sqrt 함수 사용
sqrt(2.0)             # sqrt 함수 사용

# 보통 컴퓨터에서 *(asterisk, 애스터리스크) 기호는 모든 것이라는 뜻으로 사용합니다


## 44.1.3  from import로 모듈의 일부를 가져온 뒤 이름 지정하기
## 이번에는 from import로 변수, 함수, 클래스를 가져온 뒤 이름을 지정해보겠습니다.

# from 모듈 import 변수 as 이름
# from 모듈 import 함수 as 이름
# from 모듈 import 클래스 as 이름

from math import sqrt as s    # math 모듈에서 sqrt 함수를 가져오면서 이름을 s로 지정
s(4.0)                        # s로 sqrt 함수 사용
s(2.0)                        # s로 sqrt 함수 사용

## 그럼 여러 개를 가져왔을 때 각각 이름을 지정할 수는 없을까요?
## 이때는 각 변수, 함수, 클래스 등을 콤마로 구분하여 as를 여러 개 지정하면 됩니다.

from 모듈 import 변수 as 이름1, 함수 as 이름2, 클래스 as 이름3

from math import pi as p, sqrt as s
p         # p로 원주율 출력
s(4.0)    # s로 sqrt 함수 사용
s(2.0)    # s로 sqrt 함수 사용


# 참고 | 가져온 모듈 해제하기, 다시 가져오기
# import로 가져온 모듈(변수, 함수, 클래스)은 del로 해제할 수 있습니다.
import math
del math

# 모듈을 다시 가져오려면 importlib.reload를 사용합니다.
import importlib
import math
importlib.reload(math)