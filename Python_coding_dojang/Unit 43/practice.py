### Unit 43. 정규표현식 사용하기
## 43.5 연습문제: 이메일 주소 검사하기
## 다음 소스 코드를 완성하여 주어진 이메일 주소가 올바른지 판단하도록 만드세요.
## emails 리스트에서 앞의 다섯 개는 올바른 형식이며 마지막 세 개는 잘못된 형식입니다.

import re

p = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

emails = ['python@mail.example.com', 'python+kr@example.com',         # 올바른 형식
          'python-dojang@example.co.kr', 'python_10@example.info',    # 올바른 형식
          'python.dojang@e-xample.com',                               # 올바른 형식
          '@example.com', 'python@example', 'python@example-com']     # 잘못된 형식

for email in emails:
    print(p.match(email) != None, end=' ')