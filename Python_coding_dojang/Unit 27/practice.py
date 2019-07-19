### Unit 27. 파일 사용하기
## 27.5 연습문제: 파일에서 10자 이하인 단어 개수 세기
## 단어가 줄 단위로 저장된 words.txt 파일이 주어집니다.
## 다음 소스 코드를 완성하여 10자 이하인 단어의 개수가 출력되게 만드세요.


with open('words.txt', 'r') as file:
    count = 0
    words = file.readlines()
    for word in words:
        if len(word.strip('\n')) <= 10:
            count = count + 1
    print(count)