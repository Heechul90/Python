### Unit 38. 예외 처리 사용하기
## 38.6 연습문제: 파일 예외 처리하기
## 다음 소스 코드를 완성하여 maria.txt 파일이 있으면
## 파일의 내용을 읽어서 출력하고,
## 파일이 없으면 '파일이 없습니다.'를 출력하도록 만드세요.
## 파일이 없을 때 발생하는 예외는 FileNotFoundError입니다.

try:
    file = open('maria.txt', 'r')

except:
    print('파일이 없습니다.')

else:
    s = file.read()
    file.close()

