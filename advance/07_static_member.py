class Robot:
    count = 0
    def how_count(self):
        print (f'객체 메서드: {self.count}')

    @classmethod # 원본영역의 변수를건드릴수 있다는 표시
    def std_count(cls):
        print(f'클래스 메서드 : {cls.count}')

r1 = Robot()
r2 = Robot()

#r1과 r2는 서로 다른 객체임으로count 시에 영향을 서로 받지 않는다
r1.count +=1
print(f'r1.count :{r1.count}')
print(f'r2.count :{r2.count}')
r2.count = 100
print(f'r1.count :{r1.count}')
print(f'r2.count :{r2.count}')

#원본의 내용을 고치고 싶다면? 원본으로 직접 들어가서 작업해야한다.
Robot.count = 1000
#원본영역에서의 수정은 당연히 복사본들 각각에게 영향을 미치지 못한다.
print(f'r1.count :{r1.count}')
print(f'r2.count :{r2.count}')
r1.how_count()
r2.how_count()

#마찬가지로 원본 내용을 확인하고 싶다면 원본영역에서 확인해야한다.
print(f'원본 count : {Robot.count}')

#1.원본영역에서 함수를 실행하니 self가 없다고 에러가 난다
#2. self는 내가 소속된 객체를 의미하나 원본에서 와서 객체가 없다# 3.@classmethod를 통해서 원본에서 왔다!self는 객체가 아닌 클래스이다
#4. 그러니 객체를 받는 인자로 오해받지 않기 위해서 self - cls
Robot.std_count()
