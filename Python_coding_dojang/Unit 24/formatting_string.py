### Unit 24. 문자열 응용하기
## 24.2 문자열 서식 지정자와 포매팅 사용하기
## '%s' % '문자열'
print('I am %s.' % 'james')

name = 'maria'
print('I am %s.' % name)


## 24.2.2 서식 지정자로 숫자 넣기
## '%d' % 숫자
print('I am %d years old.' % 20)


## 24.2.3 서식 지정자로 소수점 표현하기
## '%f' % 숫자
print('%f' % 2.3)

## '%.자릿수f' % 숫자
print('%.2f' % 2.3)
print('%.3f' % 2.3)


## 24.2.4 서식 지정자로 문자열 정렬하기
## %길이s
print('%10s' % 'python')

# 참고 | 자릿수가 다른 숫자 출력하기
# %길이d
print('%10d' % 150)
print('%10d' % 15000)

# %길이.자릿수f
print('%10.2f' % 2.3)
print('%10.2f' % 2000.3)

## %-길이s
print('%-10s' % 'python')


## 24.2.5 서식 지정자로 문자열 안에 값 여러 개 넣기
## '%d %s' % (숫자, '문자열')
print('Today is %d %s.' % (3, 'April'))
print('Today is %d%s.' % (3, 'April'))


## 24.2.6 format 메서드 사용하기
## '{인덱스}'.format(값)
print('Hello, {0}'.format('world!'))
print('Hello, {0}'.format(100))


## 24.2.7 format 메서드로 값을 여러 개 넣기
print('Hello, {0} {2} {1}'.format('Python', 'Script', 3.6))


## 24.2.8 format 메서드로 같은 값을 여러 개 넣기
print('{0} {0} {1} {1}'.format('Python', 'Script'))


## 24.2.9 format 메서드에서 인덱스 생략하기
print('Hello, {} {} {}'.format('Python', 'Script', 3.6))


## 24.2.10 format 메서드에서 인덱스 대신 이름 지정하기
print('Hello, {language} {version}'.format(language='Python', version=3.6))


## 24.2.11 문자열 포매팅에 변수를 그대로 사용하기
language = 'Python'
version = 3.6
print(f'Hello, {language} {version}')

# 참고 | 중괄호 출력하기
print('{{ {0} }}'.format('Python'))


## 24.2.12 format 메서드로 문자열 정렬하기
## '{인덱스:<길이}'.format(값)
print('{0:<15}'.format('python'))

## '{인덱스:>길이}'.format(값)
print('{0:>15}'.format('python'))

print('{:>10}'.format('python'))


## 24.2.13 숫자 개수 맞추기
## '%0개수d' % 숫자
## '{인덱스:0개수d'}'.format(숫자)
print('%03d' % 1)
print('{0:03d}'.format(35))

## '%0개수.자릿수f' % 숫자
## '{인덱스:0개수.자릿수f'}.format(숫자)
print('%08.2f' % 3.6)
print('{0:08.2f}'.format(150.37))


## 24.2.14 채우기와 정렬을 조합해서 사용하기
## '{인덱스:[[채우기]정렬][길이][.자릿수][자료형]}'
print('{0:0<10}'.format(15))    # 길이 10, 왼쪽으로 정렬하고 남는 공간은 0으로 채움
print('{0:0>10}'.format(15))    # 길이 10, 오른쪽으로 정렬하고 남는 공간은 0으로 채움

print('{0:0>10.2f}'.format(15))    # 길이 10, 오른쪽으로 정렬하고 소수점 자릿수는 2자리

print('{0: >10}'.format(15))    # 남는 공간을 공백으로 채움
print('{0:>10}'.format(15))     # 채우기 부분을 생략하면 공백이 들어감
print('{0:x>10}'.format(15))    # 남는 공간을 문자 x로 채움

# 참고 | 금액에서 천단위로 콤마 넣기
# format(숫자, ',')
print(format(1493500, ','))

print('%20s' % format(1493500, ','))  # 길이 20, 오른쪽으로 정렬

print('{0:,}'.format(1493500))

print('{0:>20,}'.format(1493500))     # 길이 20, 오른쪽으로 정렬
print('{0:0>20,}'.format(1493500))    # 길이 20, 오른쪽으로 정렬하고 남는 공간은 0으로 채움