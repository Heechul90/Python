### Unit 30. 함수에서 위치 인수와 키워드 인수 사용하기
## 30.7 심사문제: 가장 낮은 점수, 높은 점수와 평균 점수를 구하는 함수 만들기
## 표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다.
## 다음 소스 코드를 완성하여
## 가장 높은 점수,
## 가장 낮은 점수,
## 평균 점수가 출력되게 만드세요.
## 평균 점수는 실수로 출력되어야 합니다.

# 입력
# 76 82 89 84

# 결과
# 낮은 점수: 76.00, 높은 점수: 89.00, 평균 점수: 82.75
# 낮은 점수: 82.00, 높은 점수: 84.00, 평균 점수: 83.00

# 입력
# 89 92 73 83

# 결과
# 낮은 점수: 73.00, 높은 점수: 92.00, 평균 점수: 84.25
# 낮은 점수: 83.00, 높은 점수: 92.00, 평균 점수: 87.50


korean, english, mathematics, science = map(int, input().split())

def get_min_max_score(*args):
    return min(args), max(args)


def get_average(**kwargs):
    for args in kwargs.values():
        return sum(kwargs.values()) / len(kwargs.values())



min_score, max_score = get_min_max_score(korean, english, mathematics, science)
average_score = get_average(korean=korean, english=english,
                            mathematics=mathematics, science=science)

print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))