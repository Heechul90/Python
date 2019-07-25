### Unit 39. 이터레이터 사용하기
## 39.3 인덱스로 접근할 수 있는 이터레이터 만들기
## __getitem__ 메서드를 구현하여 인덱스로 접근할 수 있는 이터레이터를 만들어보겠습니다.

# class 이터레이터이름:
#     def __getitem__(self, 인덱스):
#         코드


class Counter:
    def __init__(self, stop):
        self.stop = stop

    def __getitem__(self, index):
        if index < self.stop:
            return index
        else:
            raise IndexError


print(Counter(3)[0], Counter(3)[1], Counter(3)[2])

for i in Counter(3):
    print(i, end=' ')