class Car:
    def start(self):
        print('시동이 걸린다')
    def run(self):
        print('차가 시속 50km로 달린다')
    def stop(self):
        print('차가 멈춘다')

class MyCar(Car):
    turbo =False
    def run(self): #부모와 동일한 이름의 매서드를 사용하면 오버라이드라고 인식된다.
        if self.turbo == True :
            print('차가 시속 200km으로 달린다')
        else:
            super().run()
mc=MyCar()
mc.start()
mc.run()
mc.turbo = True
mc.run()
mc.stop()

