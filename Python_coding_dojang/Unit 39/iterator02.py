### Unit 39. 이터레이터 사용하기
## 39.2 이터레이터 만들기

# class 이터레이터이름:
#     def __iter__(self):
#         코드
#
#     def __next__(self):
#         코드

class Counter:
    def __init__(self, stop):
        self.current = 0               # 현재 숫자 유지, 0부터 지정된 숫자 직전까지 반복
        self.stop = stop               # 반복을 끝낼 숫자

    def __iter__(self):
        return self                    # 현재 인스턴스를 반환

    def __next__(self):
        if self.current < self.stop:   # 현재 숫자가 반복을 끝낼 숫자보다 작을 때
            r = self.current           # 반환할 숫자를 변수에 저장
            self.current += 1          # 현재 숫자를 1 증가시킴
            return r                   # 숫자를 반환
        else:                          # 현재 숫자가 반복을 끝낼 숫자보다 크거나 같을 때
            raise StopIteration        # 예외 발생


for i in Counter(3):
    print(i, end=' ')



## 39.2.1  이터레이터 언패킹
## 터레이터는 언패킹(unpacking)이 가능합니다.
## 즉, 다음과 같이 Counter()의 결과를 변수 여러 개에 할당할 수 있습니다.
## 물론 이터레이터가 반복하는 횟수와 변수의 개수는 같아야 합니다.
a, b, c = Counter(3)
print(a, b, c)

a, b, c, d, e = Counter(5)
print(a, b, c, d, e)


# 참고 | 반환값을 _에 저장하는 이유
# 함수를 호출한 뒤 반환값을 저장할 때 _(밑줄 문자)를 사용하는 경우가 있습니다.
_, b = range(2)
b

a, _, c, d =  range(4)
a, c, d