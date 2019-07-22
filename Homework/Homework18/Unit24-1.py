### Unit 24. 문자열 응용하기
## 24.5 심사문제: 특정 단어 개수 세기
## 표준 입력으로 문자열이 입력됩니다.
## 입력된 문자열에서 'the'의 개수를 출력하는 프로그램을 만드세요
## (input에서 안내 문자열은 출력하지 않아야 합니다).
## 단, 모든 문자가 소문자인 'the'만 찾으면 되며
## 'them', 'there', 'their' 등은 포함하지 않아야 합니다.

## 입력
## the grown-ups' response, this time, was to advise me to lay aside my drawings of boa constrictors, whether from the inside or the outside, and devote myself instead to geography, history, arithmetic, and grammar. That is why, at the, age of six, I gave up what might have been a magnificent career as a painter. I had been disheartened by the failure of my Drawing Number One and my Drawing Number Two. Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to the.

vocas = list(map(str, input().split()))


words = []
for voca in vocas:
    if 'the' in voca:
        words.append(voca)


text = []
for word in words:
    result = word.rstrip(',.')
    if len(result) == 3:
        text.append(result)
print(len(text))
