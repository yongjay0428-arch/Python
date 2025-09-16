class Robot:
    #생성자! -> 객체화 시에 호출되는 함수의 일종으로
    #객체화가 될 때 가장 먼저 호출된다. 즉, Robot()을 부르면 init으로 호출된다.(복사 역할)
    #self?
    def __init__(self):
        print("Robot이 복사될때 제일 먼저 호출되는 멤버")

    def doit(self):
        print('나: Robot의 함수 입니다.')

robot = Robot() #객체화 -> init 호출됨
robot.doit() # 객체화 된 상태에서 실행하여 호출됨

