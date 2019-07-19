### Unit 25. 딕셔너리 응용하기
## 25.3 딕셔너리 표현식 사용하기

## 25.3.1  딕셔너리 표현식에서 if 조건문 사용하기
## dict_del_by_value_error.py 참고

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
 
for key, value in x.items():
    if value == 20:    # 값이 20이면
        del x[key]     # 키-값 쌍 삭제
 
print(x)