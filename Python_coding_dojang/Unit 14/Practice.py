### Unit 14. else를 사용하여 두 방향으로 분기하기
## 14.6 연습문제: 합격 여부 판단하기
## A 기업의 입사 시험은 필기 시험 점수가 80점 이상이면서
## 코딩 시험을 통과해야 합격이라고 정했습니다.
## (코딩 시험 통과 여부는 True, False로 구분)
## 다음 소스 코드를 완성하여 '합격', '불합격'이 출력되게 만드세요.
written_test = 75
coding_test = True

if written_test >= 80 and coding_test == True:
    print('합격')
else:
    print('불합격')