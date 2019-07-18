### Unit 24. 문자열 응용하기
## 24.4 연습문제: 파일 경로에서 파일명만 가져오기
## 다음 소스 코드를 완성하여 파일 경로에서 파일명만 출력되게 만드세요. 
## 단, 경로에서 폴더의 깊이가 달라지더라도 파일명만 출력할 수 있어야 합니다.
## python.exe

path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'

p = path.split('\\')
print(p)

print(p[0])
print(p[8])
print(p[-1])