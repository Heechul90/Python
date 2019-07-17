### Unit 21. 터틀 그래픽스로 그림 그리기
## 21.3 복잡한 도형 그리기
## 21.3.2  선으로 복잡한 무늬 그리기

import turtle as t

t.shape('turtle')
t.speed('fastest')      # 거북이 속도를 가장 빠르게 설정
for i in range(300):    # 300번 반복
    t.forward(i)        # i만큼 앞으로 이동. 반복할 때마다 선이 길어짐
    t.right(91)         # 오른쪽으로 91도 회전


# 참고 | 터틀 모양 설정하기
# 'arrow'
# 'turtle'
# 'circle'
# 'square'
# 'triangle'
# 'classic'