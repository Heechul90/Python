### Unit 21. 터틀 그래픽스로 그림 그리기
## 21.2.1  오각형 그리기

import turtle as t

t.shape('turtle')

for i in range(5):
    t.forward(100)
    t.right(360 / 5)