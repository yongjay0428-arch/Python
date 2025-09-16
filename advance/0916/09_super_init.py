class Parent():
    def __init__(self):
        print('부모 생성자 실행!')

class Child(Parent):
    def __init__(self):
        super().__init__() #원래는 생략되어있는 부모 생성자
        print('자식생성자')

ch = Child()