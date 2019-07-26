### Unit 45. 모듈과 패키지 만들기
## 45.6 연습문제: 하위 패키지 구성하기
## 다음 소스 코드를 완성하여
## from database import * 형식으로 패키지를 사용할 수 있게 만드세요.
## 여기서는 database 패키지 안에 sqlite 패키지가 들어있습니다.

from database import *

connect(':memory:')