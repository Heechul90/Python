### Unit 28. 회문 판별과 N-gram 만들기
## 28.1 회문 판별하기
## 회문(palindrome)은 순서를 거꾸로 읽어도 
## 제대로 읽은 것과 같은 단어와 문장을 말합니다

## 28.1.1  반복문으로 문자 검사하기
word = input('단어를 입력하세요: ')
 
is_palindrome = True                 # 회문 판별값을 저장할 변수, 초깃값은 True
for i in range(len(word) // 2):      # 0부터 문자열 길이의 절반만큼 반복
    if word[i] != word[-1 - i]:      # 왼쪽 문자와 오른쪽 문자를 비교하여 문자가 다르면
        is_palindrome = False        # 회문이 아님
        break
 
print(is_palindrome)                 # 회문 판별값 출력


## 28.1.2  시퀀스 뒤집기로 문자 검사하기
word = input('단어를 입력하세요: ')

print(word == word[::-1])  # 원래 문자열과 반대로 뒤집은 문자열을 비교


## 28.1.3  리스트와 reversed 사용하기
word = 'level'
list(word) == list(reversed(word))

list(word)
list(reversed(word))


## 28.1.4  문자열의 join 메서드와 reversed 사용하기
word = 'level'
word == ''.join(reversed(word))


word
''.join(reversed(word))