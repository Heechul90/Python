### Unit 35. 클래스 속성과 정적, 클래스 메서드 사용하기
## 35.5 연습문제: 날짜 클래스 만들기
## 다음 소스 코드에서 Date 클래스를 완성하세요.
## is_date_valid는 문자열이 올바른 날짜인지 검사하는 메서드입니다.
## 날짜에서 월은 12월까지 일은 31일까지 있어야 합니다.

# 실행 결과
# 올바른 날짜 형식입니다.

class Date:
    @staticmethod
    def is_date_valid(date_string):
        year, month, day = map(int, date_string.split('-'))
        return month <= 12 and day <= 31




if Date.is_date_valid('2000-10-32'):
    print('올바른 날짜 형식입니다.')
else:
    print('잘못된 날짜 형식입니다.')