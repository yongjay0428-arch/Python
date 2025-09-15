
class Puppy:
    name="" #멤버변수(필드) - class 안에서 사용가능한 변수임
    goal=""
    def __init__(self,name,goal): #객체화시에 호출되는 함수, 최초에 한번 불러짐
        #받아온 네임과 골은 생성자를 벗어나지 못한다.
        #따라서 객체에다가 넣어줘야 객체 지속기간동안 사용 가능하다
        # name=name으로는 어떤게 객체 멤버인지 몰라서 self을 통해 표시한다
        #다른 언어에서는 오류 방지 위한 권장 사항이지만 파이썬은 한줄씩 실행해서 진짜 모름
        self.name=name
        self.goal=goal

puppy=Puppy("멍멍이","집지키기")


