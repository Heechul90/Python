### Unit 22. 리스트와 튜플 응용하기
## 22.4 리스트의 가장 작은 수, 가장 큰 수, 합계 구하기
a = [38, 21, 53, 62, 19]
smallest = a[0]
print(smallest)
for i in a:
    if i < smallest:
        smallest = i

print(smallest)


a = [38, 21, 53, 62, 19]
largest = a[0]
for i in a:
    if i > largest:
        largest = i

print(largest)


a = [38, 21, 53, 62, 19]
a.sort()
print(a[0])
print(a[-1])

a = [38, 21, 53, 62, 19]
a.sort(reverse = True)
print(a[-1])
print(a[0])



a = [38, 21, 53, 62, 19]
print(min(a))
print(max(a))


## 22.4.2  요소의 합계 구하기
a = [10, 10, 10, 10, 10]
x = 0
for i in a:
    x += i

print(x)


a = [10, 10, 10, 10, 10]
print(sum(a))