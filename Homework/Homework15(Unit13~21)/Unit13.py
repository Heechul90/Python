### Unit 13. if 조건문으로 특정 조건일 때 코드 실행하기
## 13.7 심사문제: 온라인 할인 쿠폰 시스템 만들기
## 표준 입력으로 가격(정수)과 쿠폰 이름이 각 줄에 입력됩니다. 
## Cash3000 쿠폰은 3,000원, Cash5000 쿠폰은 5,000원을 할인합니다. 
## 쿠폰에 따라 할인된 가격을 출력하는 프로그램을 만드세요
## (input에서 안내 문자열은 출력하지 않아야 합니다).

price = int(input("Price: "))
coupon = int(input("Cash3000 = 1 or Cash5000 = 2 가지고 있는 쿠폰을 입력하시오.: "))

if coupon == 1:
    print(price - 3000)
elif coupon == 2:
    print(price - 5000)
else:
    print("다시 입력하시오.")