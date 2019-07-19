### Unit 26. 세트 사용하기
## 26.8 연습문제: 공배수 구하기
## 다음 소스 코드를 완성하여 1부터 100까지 숫자 중 
## 3과 5의 공배수를 세트 형태로 출력되게 만드세요.
## {75, 45, 15, 90, 60, 30}

a = {i for i in range(1, 101) if i % 3 == 0}
b = {i for i in range(1, 101) if i % 5 == 0}

print(a)
print(b)

print(a & b)
print(set.intersection(a, b))

