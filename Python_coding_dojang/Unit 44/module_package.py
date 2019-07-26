### Unit 44. 모듈과 패키지 사용하기
## 44.2 import로 패키지 가져오기
## 패키지는 특정 기능과 관련된 여러 모듈을 묶은 것인데,
## 패키지에 들어있는 모듈도 import를 사용하여 가져옵니다.

# import 패키지.모듈
# import 패키지.모듈1, 패키지.모듈2
# 패키지.모듈.변수
# 패키지.모듈.함수()
# 패키지.모듈.클래스()

# 여기서는 파이썬 표준 라이브러리에서 urllib 패키지의 request 모듈을 가져와보겠습니다
# (urllib은 URL 처리에 관련된 모듈을 모아 놓은 패키지입니다).

import urllib.request
response = urllib.request.urlopen('http://www.google.co.kr')
response.status

# 참고 | urlopen 함수
# urllib.request.urlopen은 URL을 여는 함수인데
# URL 열기에 성공하면 response.status의 값이 200이 나옵니다.
# 이 200은 HTTP 상태 코드이며 웹 서버가 요청을 제대로 처리했다는 뜻입니다.


## 44.2.1  import as로 패키지 모듈 이름 지정하기
## 패키지 안에 들어있는 모듈도 import as를 사용하여 이름을 지정할 수 있습니다.

# import 패키지.모듈 as 이름

import urllib.request as r    # urllib 패키지의 request 모듈을 가져오면서 이름을 r로 지정
response = r.urlopen('http://www.google.co.kr')    # r로 urlopen 함수 사용
response.status


## 44.2.2  from import로 패키지의 모듈에서 일부만 가져오기
## 패키지도 from import를 사용하여 모듈에서 변수, 함수, 클래스를 가져올 수 있습니다.

# from 패키지.모듈 import 변수
# from 패키지.모듈 import 함수
# from 패키지.모듈 import 클래스
# from 패키지.모듈 import 변수, 함수, 클래스

from urllib.request import Request, urlopen    # urlopen 함수, Request 클래스를 가져옴
req = Request('http://www.google.co.kr')       # Request 클래스를 사용하여 req 생성
response = urlopen(req)                        # urlopen 함수 사용


## 패키지의 모듈에서 모든 변수, 함수, 클래스를 가져오는 방법은 다음과 같습니다.

# from 패키지.모듈 import *

from urllib.request import *                # urllib의 request 모듈에서 모든 변수, 함수, 클래스를 가져옴
req = Request('http://www.google.co.kr')    # Request를 사용하여 req 생성
response = urlopen(req)                     # urlopen 함수 사용
response.status


## 44.2.3  from import로 패키지의 모듈의 일부를 가져온 뒤 이름 지정하기
## 이번에는 from import로 패키지의 모듈에서 변수, 함수, 클래스를 가져온 뒤 이름을 지정해보겠습니다.

# from 패키지.모듈 import 변수 as 이름
# from 패키지.모듈 import 변수 as 이름, 함수 as 이름, 클래스 as 이름

from urllib.request import Request as r, urlopen as u
req = r('http://www.google.co.kr')    # r로 Request 클래스 사용
response = u(req)                     # u로 urlopen 함수 사용
response.status