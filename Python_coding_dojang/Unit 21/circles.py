### Unit 21. 터틀 그래픽스로 그림 그리기
## 21.3 복잡한 도형 그리기
## 21.3.1  원을 반복해서 그리기

import turtle as t


n = 60    # 원을 60번 그림
t.shape('turtle')
t.speed('fastest')      # 거북이 속도를 가장 빠르게 설정
for i in range(n):
    t.circle(120)       # 반지름이 120인 원을 그림
    t.right(360 / n)    # 오른쪽으로 6도 회전
t.mainloop()



## 속도
## 'fastest': 0
## 'fast': 10
## 'normal': 6
## 'slow': 3
## 'slowest': 1