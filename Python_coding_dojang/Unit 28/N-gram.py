### Unit 28. 회문 판별과 N-gram 만들기
## 28.2.1  반복문으로 N-gram 출력하기

text = 'Hello'

for i in range(len(text) - 1):  # 2-gram이므로 문자열의 끝에서 한 글자 앞까지만 반복함
    print(text[i], text[i + 1], sep='')  # 현재 문자와 그다음 문자 출력


text = 'this is python script'
words = text.split()  # 공백을 기준으로 문자열을 분리하여 리스트로 만듦
print(words)

for i in range(len(words) - 1):  # 2-gram이므로 리스트의 마지막에서 요소 한 개 앞까지만 반복함
    print(words[i], words[i + 1])  # 현재 문자열과 그다음 문자열 출력



## 28.2.2  zip으로 2-gram 만들기
text = 'hello'

two_gram = zip(text, text[1:])
print(two_gram)

for i in two_gram:
    print(i[0], i[1], sep='')


text = 'hello'
list(zip(text, text[1:]))


text = 'this is python script'
words = text.split()
list(zip(words, words[1:]))


## 28.2.3  zip과 리스트 표현식으로 N-gram 만들기
text = 'hello'
[text[i:] for i in range(3)]


list(zip(['hello', 'ello', 'llo']))


list(zip(*['hello', 'ello', 'llo']))
