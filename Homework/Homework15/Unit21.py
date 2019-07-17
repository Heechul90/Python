### Unit 21. 터틀 그래픽스로 그림 그리기
## 21.5 연습문제: 오각별 그리기
## 다음 소스 코드를 완성하여 오각별이 그려지게 만드세요.

## 각 변의 길이는 100
## 별의 꼭지점은 72도를 두 번 회전해서 144도 회전
## 별의 다음 꼭지점을 그릴 때는 72도 회전

import turtle as t

t.shape('turtle')
for i in range(5):
    t.fd(100)
    t.right(360 - 72)
    t.fd(100)
    t.right(72 * 2)
t.mainloop()
