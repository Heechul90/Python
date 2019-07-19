### Unit 28. 회문 판별과 N-gram 만들기
## 28.3 연습문제: 단어 단위 N-gram 만들기
## 표준 입력으로 정수와 문자열이 각 줄에 입력됩니다.
## 다음 소스 코드를 완성하여 입력된 숫자에 해당하는 단어
## 단위 N-gram을 튜플로 출력하세요(리스트 표현식 사용).
## 만약 입력된 문자열의 단어 개수가 입력된 정수 미만이라면 'wrong'을 출력하세요.

n = int(input())
text = input()
words = text.split()

if len(words) < n:
    print('wrong')
else:
    n_gram = zip(*[words[i:] for i in range(n)])
    for i in n_gram:
        print(i)