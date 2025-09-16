class Robot():
    count = 0
    def how_count(self):
        print (f'객체 메서드: {self.count}')

    def std_count(self):
        print(f'클래스 메서드 : {self.count}')

r1 = Robot()
r2 = Robot()

#r1과 r2는 서로 다른 객체임으로count 시에 영향을 서로 받지 않는다
r1.count +=1
print(f'r1.count :{r1.count}')
print(f'r2.count :{r2.count}')
r2.count = 100
print(f'r1.count :{r1.count}')
print(f'r2.count :{r2.count}')