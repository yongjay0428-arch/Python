# java에서는 파일명 == 클래스 명
# 하지만 파이썬에서는 꼭 그런건 아니다.
class Student: # Student 라는 클래스(학생과 관련된 함수 및 면수가 들어오겠구나 라고 예측 가능)
    pass # pass는 함수나 클래스에 아무것도 없을시에 오류 방지 차원에서 넣는 키워드(선언및사용)

std1 = Student()
std2 = Student()
std3 = Student()
#일련번호가 서로 다르다
#파이썬에서도 객체화는 복사를 의미함으로 서로 다른 객체는 같지 않다.
print(std1)
print(std2)
print(std3)