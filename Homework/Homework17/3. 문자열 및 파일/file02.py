### 문자열 및 파일
## 문제 2
## 시저 암호는, 고대 로마의 황제 줄리어스 시저가 만들어 낸 암호인데,
## 예를 들어 알파벳 A를 입력했을 때,
## 그 알파벳의 n개 뒤에 오는 알파벳이 출력되는 것이다.
## 예를 들어 바꾸려는 단어가 'CAT"고,
## n을 5로 지정하였을 때 "HFY"가 되는 것이다.
## 어떠한 암호를 만들 문장과 n을 입력했을 때
## 암호를 만들어 출력하는 프로그램을 작성하시오.

# 입력 : 화면에서 문자열과 n값을 입력받는다. (예: ROSE 5)
# 출력 : 암호화된 문자열을 출력

plain, n = input('문자열, N값: ').split()

a = []
for i in plain:
    a.append(i)
a
n = int(n)

LETTER_A = ord('A')     # 변수명을 대문자로 하면 상수(Constant) 취급을 하게 됨.
LETTER_Z = ord('Z')
cypher = []
for letter in a:
    if ord(letter) + n > LETTER_Z:
        cypher.append(chr(LETTER_A + ord(letter) + n - LETTER_Z - 1))
    else:
        cypher.append(chr(ord(letter) + n))
print(''.join(cypher))
