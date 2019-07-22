### Unit 24. 문자열 응용하기
## 24.1 문자열 조작하기
## 문자열은 문자열을 조작하거나 정보를 얻는 다양한 메서드(method)를 제공합니다

## 24.1.1  문자열 바꾸기
## replace('바꿀문자열', '새문자열')은 문자열 안의 문자열을 다른 문자열로 바꿉니다
print('Hello, world!'.replace('world', 'Python'))

s = "Hello, world!"
s = s.replace('world!', 'Python')
print(s)


## 24.1.2  문자 바꾸기
## str.maketrans('바꿀문자', '새문자')로 변환 테이블을 만듭니다
## translate(테이블)을 사용하면 문자를 바꾼 뒤 결과를 반환합니다
table = str.maketrans('aeiou', '12345')
print('apple'.translate(table))


## 24.1.3  문자열 분리하기
## split()은 공백을 기준으로 문자열을 분리하여 리스트로 만듭니다
print('apple pear grape pineapple orange'.split())

## split('기준문자열')과 같이 기준 문자열을 지정하면 기준 문자열로 문자열을 분리합니다
print('apple, pear, grape, pineapple, orange'.split(', '))


## 24.1.4  구분자 문자열과 문자열 리스트 연결하기
## join(리스트)는 구분자 문자열과 문자열 리스트의 요소를 연결하여 문자열로 만듭니다.
print(' '.join(['apple', 'pear', 'grape', 'pineapple', 'orange']))
print('-'.join(['apple', 'pear', 'grape', 'pineapple', 'orange']))


## 24.1.5  소문자를 대문자로 바꾸기
## upper()는 문자열의 문자를 모두 대문자로 바꿉니다.
print('python'.upper())


## 24.1.6  대문자를 소문자로 바꾸기
## lower()는 문자열의 문자를 모두 소문자로 바꿉니다.
print('PYTHON'.lower())


## 24.1.7  왼쪽 공백 삭제하기
## lstrip()은 문자열에서 왼쪽에 있는 연속된 모든 공백을 삭제합니다(l은 왼쪽(left)을 의미)
print('   Python   '.lstrip())


## 24.1.8  오른쪽 공백 삭제하기
## rstrip()은 문자열에서 오른쪽에 있는 연속된 모든 공백을 삭제합니다(r은 오른쪽(right)을 의미).
print('   Python   '.rstrip())


## 24.1.9  양쪽 공백 삭제하기
## strip()은 문자열에서 양쪽에 있는 연속된 모든 공백을 삭제합니다.
print('   Python   '.strip())


## 24.1.10 왼쪽의 특정 문자 삭제하기
## lstrip('삭제할문자들')과 같이 삭제할 문자들을 문자열 형태로 넣어주면 
## 문자열 왼쪽에 있는 해당 문자를 삭제합니다.
print(', python.'.lstrip(',.'))


## 24.1.11 오른쪽의 특정 문자 삭제하기
## rstrip('삭제할문자들')과 같이 삭제할 문자들을 문자열 형태로 넣어주면 
## 문자열 오른쪽에 있는 해당 문자를 삭제합니다. 
print(', python.'.rstrip(',.'))


## 24.1.12 양쪽의 특정 문자 삭제하기
## strip('삭제할문자들')과 같이 삭제할 문자들을 문자열 형태로 넣어주면 
## 문자열 양쪽에 있는 해당 문자를 삭제합니다.
print(', python.'.strip(',.'))

# 참고 | 구두점을 간단하게 삭제하기
import string
print(', python.'.strip(string.punctuation))
print(string.punctuation)

print(', python.'.strip(string.punctuation + ' '))
print(', python.'.strip(string.punctuation).strip())


## 24.1.13 문자열을 왼쪽 정렬하기
## ljust(길이)는 문자열을 지정된 길이로 만든 뒤 왼쪽으로 정렬하며 
## 남는 공간을 공백으로 채웁니다(l은 왼쪽(left)을 의미)
print('python'.ljust(10))


## 24.1.14 문자열을 오른쪽 정렬하기
## rjust(길이)는 문자열을 지정된 길이로 만든 뒤 오른쪽으로 정렬하며 
## 남는 공간을 공백으로 채웁니다(r은 오른쪽(right)을 의미)
print('python'.rjust(10))


## 24.1.15 문자열을 가운데 정렬하기
## center(길이)는 문자열을 지정된 길이로 만든 뒤 가운데로 정렬하며 
## 남는 공간을 공백으로 채웁니다
print('python'.center(10))
print('python'.center(11))


## 24.1.16 메서드 체이닝
print('python'.rjust(10).upper())


## 24.1.17 문자열 왼쪽에 0 채우기
## zfill(길이)는 지정된 길이에 맞춰서 
## 문자열의 왼쪽에 0을 채웁니다( zero fill을 의미)
print('35'.zfill(4))        # 숫자 앞에 0을 채움
print('3.5'.zfill(6))       # 숫자 앞에 0을 채움
print('hello'.zfill(10))    # 문자열 앞에 0을 채울 수도 있음


## 24.1.18 문자열 위치 찾기
## find('찾을문자열')은 문자열에서 특정 문자열을 찾아서 인덱스를 반환하고, 
## 문자열이 없으면 -1을 반환합니다
print('apple pineapple'.find('pl'))
print('apple pineapple'.find('xy'))


## 24.1.19 오른쪽에서부터 문자열 위치 찾기
## rfind('찾을문자열')은 오른쪽에서부터 특정 문자열을 찾아서 인덱스를 반환하고, 
## 문자열이 없으면 -1을 반환합니다(r은 오른쪽( right)을 의미)
print('apple pineapple'.rfind('pl'))
print('apple pineapple'.rfind('xy'))


## 24.1.20 문자열 위치 찾기
## index('찾을문자열')은 왼쪽에서부터 특정 문자열을 찾아서 인덱스를 반환합니다. 
## 단, 문자열이 없으면 에러를 발생시킵니다
print('apple pineapple'.index('pl'))


## 24.1.21 오른쪽에서부터 문자열 위치 찾기
## rindex('찾을문자열')은 오른쪽에서부터 특정 문자열을 찾아서 인덱스를 반환합니다
## (r은 오른쪽(right)을 의미)
print('apple pineapple'.rindex('pl'))


## 24.1.22 문자열 개수 세기
## count('문자열')은 현재 문자열에서 특정 문자열이 몇 번 나오는지 알아냅니다
print('apple pineapple'.count('pl'))