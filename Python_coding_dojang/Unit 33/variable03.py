### Unit 33. 클로저 사용하기
## 33.3 클로저 사용하기

def calc():
    a = 3
    b = 5

    def mul_add(x):
        return a * x + b  # 함수 바깥쪽에 있는 지역 변수 a, b를 사용하여 계산

    return mul_add        # mul_add 함수를 반환


c = calc()
print(c(1), c(2), c(3), c(4), c(5))



## 33.3.2  클로저의 지역 변수 변경하기
def calc():
    a = 3
    b = 5
    total = 0

    def mul_add(x):
        nonlocal total
        total = total + a * x + b
        print(total)

    return mul_add


c = calc()
c(1)
c(2)
c(3)