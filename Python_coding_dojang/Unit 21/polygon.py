### Unit 21. 터틀 그래픽스로 그림 그리기
## 21.2.2  다각형 그리기

import turtle as t

t.shape('turtle')

n = int(input('숫자를 입력하시오.: '))

for i in range(n):
    t.forward(100)
    t.right(360 / n)
t.mainloop()