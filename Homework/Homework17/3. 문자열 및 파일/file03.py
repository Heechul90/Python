### 문자열 및 파일
## 문제 2
## Linux 명령어인 grep 을 윈도우스에서 만들어 보시오.
## 입력 형태
## 찾을 문자열: public
## 찾을 파일명: f:/Workspace/Egov/xxx.java

## 출력 형태
## 13: public class ClassA {
## 16:     public int number;


word, filename = input('찾고자 하는 문자열과 파일명: ').split()

lineNo = 1
with open(filename, 'r', encoding='UTF-8') as file:
    for line in file:
        if line.find(word) >= 0:
            print('%3d:' % lineNo, line, end='')
        lineNo += 1