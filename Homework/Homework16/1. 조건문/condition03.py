### 조건문
## 문제 03
## 세 정수 a, b, c를 입력으로 받아 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오.

a, b, c = map(int, input('정수를 입력하시오.: ').split())

if a > b and a > c:
    if b > c:
        print(b)
    elif b > c:
        print(c)
    else:
        print('b와 c는 같습니다!')

elif b > a and b > c:
    if a > c:
        print(a)
    elif c > a:
        print(c)
    else:
        print('a와 c는 같습니다!')

elif c > a and c > b:
    if a > b:
        print(a)
    elif b > a:
        print(b)
    else:
        print('b와 c는 같습니다')

else:
    print('다시 입력하세요~!')
