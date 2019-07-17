### Unit 15. elif를 사용하여 여러 방향으로 분기하기
## 15.4 심사문제: 교통카드 시스템 만들기
## 표준 입력으로 나이(만 나이)가 입력됩니다(입력 값은 7 이상 입력됨).
## 교통카드 시스템에서 시내버스 요금은 다음과 같으며 
## 각 나이에 맞게 요금을 차감한 뒤 잔액이 출력되게 만드세요(if, elif 사용).
## 현재 교통카드에는 9,000원이 들어있습니다.

# 어린이(초등학생, 만 7세 이상 12세 이하): 650원
# 청소년(중∙고등학생, 만 13세 이상 18세 이하): 1,050원
# 어른(일반, 만 19세 이상): 1,250원

age = int(input("당신의 나이를 입력하시오.:"))
balance = 9000

c = 650         # children
y = 1050        # youth
a = 1250        # adult

if 7 <= age <= 12:
    balance -= c
elif 13 <= age <= 18:
    balance -= y
elif age >= 19:
    balance -= a
    
print(balance)