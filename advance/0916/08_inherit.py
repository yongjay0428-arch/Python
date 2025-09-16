class Runner:
    def run(self):
        print('뛴다')
    def sprint(self):
        print('전력으로 뛴다')
class Jumper:
    def jump(self):
        print('점프한다')
    def high_jump(self):
        print('높이 점프를한다')
class Person(Jumper, Runner): #Jumper와 Runner를 상속받았다
    def walk(self):
        print('걷는다')
#walk 사용 위해 person 객체화
p = Person()
p.walk()
#상속함수들을 내것처럼 사용할 수 있다
p.run()
p.sprint()
p.jump()
p.high_jump()