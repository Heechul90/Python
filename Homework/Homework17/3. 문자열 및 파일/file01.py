### 문자열 및 파일
## 문제 1
## 앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이 같은 수를 대칭수(palindrome)라고 부른다.
## 두 자리 수를 곱해 만들 수 있는 대칭수 중 가장 큰 수는 9009 (= 91 × 99) 이다.
## 세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수는 얼마인가?


def isPalindrome(a):
    for i in range(len(a)//2):
        if a[i] != a[-1-i]:
            return False
    return True

maxNum = 0
for i in range(100, 1000):
    for k in range(i, 1000):
        if isPalindrome(str(i*k)):
            if i*k > maxNum:
                maxNum = i*k
                maxA = i
                maxB = k
print(maxNum, maxA, maxB)


