class Car:
    # member 변수 필드
    gear = 0
    on = False
    #생성자 -  #객체화를 위해서 필수적임
    #그러나 프로그래밍의 규칙중 하나는 너무 당연한건 생략이 가능하다는 것!
    def __init__(self,gear,on):
        #혹시나 기어가 들어가 있거나 시동이 켜져있는 경우가 있을수도 -> 초기상태로 되돌린다.
        self.gear =0
        self.on = False
    #멤버 함수 - 클래스 안의 생성자 함수들은 해당 객체 표시를 하기 위한 self를 기본으로 가진다
    def start(self):
        if not self.on:
            print('시동이 걸렸습니다.')
            self.on = True
        else:
            print('시동이 이미 걸려있습니다.')
    def change(self,gear):
        print(f'{self.gear}단으로 변속했습니다.')
        self.gear += gear
