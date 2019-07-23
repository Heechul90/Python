### Unit 33. 클로저 사용하기
## 33.1 변수의 사용 범위 알아보기
x = 10        # 전역 변수

def foo():
    print(x)  # 전역 변수 출력

foo()
print(x)      # 전역 변수 출력

# 그럼 변수 x를 함수 foo 안에서 만들면 어떻게 될까요?
def foo():
    x = 10    # foo의 지역 변수
    print(x)  # foo의 지역 변수 출력


foo()
print(x)      # 에러. foo의 지역 변수는 출력할 수 없음


## 33.1.1  함수 안에서 전역 변수 변경하기
x = 10        # 전역 변수

def foo():
    x = 20    # x는 foo의 지역 변수
    print(x)  # foo의 지역 변수 출력

foo()
print(x)      # 전역 변수 출력


# global 전역변수
x = 10        # 전역 변수

def foo():
    global x  # 전역 변수 x를 사용하겠다고 설정
    x = 20    # x는 전역 변수
    print(x)  # 전역 변수 출력

foo()
print(x)      # 전역 변수 출력


# 전역 변수 x가 없는 상태
def foo():
    global x  # x를 전역 변수로 만듦
    x = 20    # x는 전역 변수
    print(x)  # 전역 변수 출력


foo()
print(x)      # 전역 변수 출력


# 참고 | 네임스페이스
# 파이썬에서 변수는 네임스페이스(namespace, 이름공간)에 저장됩니다.
x = 10
locals()

def foo():
    x = 10
    print(locals())

foo()
