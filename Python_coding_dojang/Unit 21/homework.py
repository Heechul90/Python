### Unit 21. 터틀 그래픽스로 그림 그리기
## 21.6 심사문제: 별 그리기
## 표준 입력으로 꼭지점 개수(정수)와 
## 선의 길이(정수)가 입력됩니다(꼭지점 개수의 입력 범위는 5~10, 
## 선의 길이 입력 범위는 50~150입니다). 
## 다음 소스 코드를 완성하여 꼭지점 개수와 선의 길이에 맞는 별이 그려지게 만드세요. 별을 그릴 때는 현재 위치부터 오른쪽으로 이동해서 시작해야 하며 시계 방향으로 그려야 합니다.

import turtle as t

vertex = int(input('꼭지점의 갯수(5~10)를 입력하시오.: '))
line = int(input('선의 길이(50~150)을 입력하시오.: '))

t.shape('turtle')
for i in range(vertex):
    t.fd(line)
    t.right(360 - (360/vertex))
    t.fd(line)
    t.right((360/vertex)*2)

t.mainloop()

