### Unit 27. 파일 사용하기
## 27.1 파일에 문자열 쓰기, 읽기
import os
os.getcwd()                                                              # 현재 디렉토리 위치를 출력
os.chdir('D:\\Heechul\\Python_lecture\\Python_coding_dojang\\Unit 27')   # change directory, 경로는 '\'
# os.mkdir('경로')  폴더 만들기
# 파일 이동

import shutil  # 모듈 사용
# 파일 복사
# 파일 이동
# shutil.move(a, b)



## 27.1.1  파일에 문자열 쓰기
## 파일객체 = open(파일이름, 파일모드)
## 파일객체.write('문자열')
## 파일객체.close()
file = open('hello.txt', 'w')    # hello.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 반환
file.write('Hello, world!')      # 파일에 문자열 저장
file.close()                     # 파일 객체 닫기


## 27.1.2  파일에서 문자열 읽기
## 변수 = 파일객체.read()
file = open('hello.txt', 'r')    # hello.txt 파일을 읽기 모드(r)로 열기. 파일 객체 반환
s = file.read()                  # 파일에서 문자열 읽기
print(s)                         # Hello, world!
file.close()                     # 파일 객체 닫기


## 27.1.3  자동으로 파일 객체 닫기
## with open(파일이름, 파일모드) as 파일객체:
##    코드
with open('hello.txt', 'r') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
    s = file.read()                     # 파일에서 문자열 읽기
    print(s)                            # Hello, world!
