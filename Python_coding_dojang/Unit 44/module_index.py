### Unit 44. 모듈과 패키지 사용하기
## 파이썬은 파이썬 표준 라이브러리(Python Standard Library, PSL) 이외에도
## 파이썬 패키지 인덱스(Python Package Index, PyPI)를 통해 다양한 패키지를 사용할 수 있습니다.

## 44.3.1  pip 설치하기
## pip는 파이썬 패키지 인덱스의 패키지 관리 명령어이며 Windows용 파이썬에는 기본으로 내장되어 있습니다.
## 리눅스와 macOS에서는 콘솔(터미널)에서 다음과 같은 방법으로 설치하면 됩니다.


## 44.3.2  pip로 패키지 설치하기
## 이제 pip install 명령으로 패키지를 설치해보겠습니다.

# pip install 패키지


## 44.3.3  import로 패키지 가져오기
## 이제 파이썬 코드에서 패키지를 사용해보겠습니다.

# import 패키지

import requests                                # pip로 설치한 requests 패키지를 가져옴
r = requests.get('http://www.google.co.kr')    # requests.get 함수 사용
r.status_code