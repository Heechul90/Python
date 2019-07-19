### Unit 27. 파일 사용하기
## 27.2 문자열 여러 줄을 파일에 쓰기, 읽기

## 27.2.1  반복문으로 문자열 여러 줄을 파일에 쓰기
with open('hello.txt', 'w') as file:    # hello.txt 파일을 쓰기 모드(w)로 열기
    for i in range(3):
        file.write('Hello, world! {0}\n'.format(i))


## 27.2.2  리스트에 들어있는 문자열을 파일에 쓰기            
## 파일객체.writelines(문자열리스트)
lines = ['안녕하세요.\n', '파이썬\n', '코딩 도장입니다.\n']

with open('hello.txt', 'w') as file:    # hello.txt 파일을 쓰기 모드(w)로 열기
    file.writelines(lines)


## 27.2.3  파일의 내용을 한 줄씩 리스트로 가져오기
## 변수 = 파일객체.readlines()
with open('hello.txt', 'r') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
    lines = file.readlines()
    print(lines)


## 27.2.4  파일의 내용을 한 줄씩 읽기
with open('hello.txt', 'r') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
    line = None                         # 변수 line을 None으로 초기화
    while line != '':
        line = file.readline()
        print(line.strip('\n'))         # 파일에서 읽어온 문자열에서 \n 삭제하여 출력


## 27.2.5  for 반복문으로 파일의 내용을 줄 단위로 읽기
with open('hello.txt', 'r') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
    for line in file:                   # for에 파일 객체를 지정하면 파일의 내용을 한 줄씩 읽어서 변수에 저장함
        print(line.strip('\n'))         # 파일에서 읽어온 문자열에서 \n 삭제하여 출력

# 참고 | 파일 객체는 이터레이터
# 파일 객체는 이터레이터입니다. 
# 따라서 변수 여러 개에 저장하는 언패킹(unpacking)도 가능합니다
file = open('hello.txt', 'r')  
a, b, c = file
print(a, b, c)

file.close()