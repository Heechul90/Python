### Unit 9. 문자열 사용하기
## 9.1 문자열 사용하기

hello = 'Hello, world'
print(hello)

hello = '안녕하세요'
print(hello)

hello = "Hello, world"
print(hello)

hello = '''Hello, Python!'''
print(hello)

python = """Python Programming"""
print(python)


## 9.1.1 여러 줄로 된 문자열 사용하기
hello = '''Hello, world!
안녕하세요.
Python입니다!'''

print(hello)


## 9.1.2 문자열 안에 작은따옴표나 큰따옴표 포함하기
s = "Python isn't difficult"
print(s)

# s = 'Python isn't difficult'
# SyntaxError: invalid syntax
# s = "He said "Python is easy""
# SyntaxError: invalid syntax

single_quote = '''"Hello there"
I am Python'''

double_quote = """"안녕하세요."
'파이썬'입니다."""

double_quote2 = """Hello, 'Python'"""    # 한 줄로 작성
 

print(single_quote)
print(double_quote)
print(double_quote2)

# 참고 | 문자열에 따옴표를 포함하는 다른 방법
print('Python isn\'t difficult')
    
# 참고 | 따옴표 세 개로 묶지 않고 여러 줄로 된 문자열 사용하기
print('Hello\nPython')

# >>> '''Hello
# Python'''
# 'Hello\nPython'

