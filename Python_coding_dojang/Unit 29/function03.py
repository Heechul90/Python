### Unit 29. 함수 사용하기
## 29.3 함수의 결과를 반환하기
## def 함수이름(매개변수):
##     return 반환값

def add(a, b):
    return a + b

x = add(10, 20)
print(x)

print(add(10, 20))

# 참고 | 매개변수는 없고 반환값만 있는 함수
def one():
    return 1

x = one()
print(x)

# 참고 | return으로 함수 중간에서 빠져나오기
def not_ten(a):
    if a == 10:
        return
    print(a, '입니다', sep = '')

not_ten(5)
not_ten(10)


# 성적 반환 함수
def grade(score):
    if score >= 90:
        gr = 'A'
    elif score >= 80:
        gr = 'B'
    elif score >= 70:
        gr = 'C'
    elif score >= 60:
        gr = 'D'
    else:
        gr = 'F'
    return gr
grade(100)

def grade2(score):
    if score >= 90:
        return 'A'
    if score >= 80:
        return 'B'
    if score >= 70:
        return 'C'
    if score >= 60:
        return 'D'
    return 'F'
grade2(100)