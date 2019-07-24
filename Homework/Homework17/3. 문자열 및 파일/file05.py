### 문자열 및 파일
## 문제 2
## 다음의 지시대로 폴더와 파일을 프로그램에서 만드시오.

# 랜덤으로 1, 2, 3 중 하나를 내용으로 갖는 txt 파일100개를
# 하나의 디렉토리(c:/Temp/Ex04) 안에 생성하는 코드를 작성하시오.
# (파일 제목은 4자리 정수를 랜덤으로 할당.
# ex - 1382.txt , 0201.txt , 9012.txt , ......... )

# 제목이 0000~3333 인 txt 파일은 low 폴더로,
# 3334~6666인 txt 파일은 mid 폴더로,
# 6667~9999 인 파일은 high 폴더로 이동시키는 코드를 작성하시오.

# low, mid, high 폴더 안에 제목이 1, 2, 3 인 폴더를 각각 만들고,
# txt 파일 안의 내용에 따라 txt파일을 폴더안으로 이동시켜 분류하시오.

# 결론적으로 c:/Temp/Ex04 폴더 밑에는 low, mid, high 폴더 3개가 생기고,
# 이 각각의 폴더에는 1, 2, 3 폴더가 각각 생기고 이 폴더밑에 파일이 들어 있어야 함.

import os
import shutil
import random as rd
PATH = 'c:/Temp/Ex04'
os.mkdir(PATH)
os.chdir(PATH)
for dirname in ('low', 'mid', 'high'):
    os.mkdir(PATH + '/' + dirname)
    for num in ('1', '2', '3'):
        os.mkdir(PATH + '/' + dirname + '/' + num)

for i in range(100):
    filenumber = rd.randint(0, 9999)
    content = str(rd.randint(1, 3))
    filename = '%04d.txt' % filenumber
    file = open(filename, 'w')
    file.write(content)
    file.close()

fileList = os.listdir(PATH)
for filename in fileList:
    # 디렉토리면 처리하지 않고 Loop을 반복
    if os.path.isdir(filename):
        continue

    # 일반 파일이면
    # 파일이름에서 숫자를 구하고, 파일을 읽어서 콘텐츠를 가져온다.
    filenumber = int(filename[0:4])     # '1234.txt'로 부터 1234를 구함
    file = open(filename, 'r')
    content = file.read(1)
    file.close()

    # 원하는 위치에 파일을 이동
    if filenumber <= 3333:
        dirname = 'low'
    elif filenumber <= 6666:
        dirname = 'mid'
    else:
        dirname = 'high'
    dst = dirname + '/' + content + '/' + filename
    shutil.move(filename, dst)
