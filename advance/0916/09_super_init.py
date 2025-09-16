class Parent():
    def __init__(self):
        print('부모 생성자 실행!')

class Child(Parent):
    def __init__(self):
        super().__init__() #원래는 생략되어있는 부모 생성자
        print('자식생성자')

ch = Child()

#부모가 초기화가 필요하다면 자식에게 값을 전달해서 자식이 부모에게 전달하도록 한다.
class SchoolMember(): #클래스만 스네이크 사용 X
    name = ''
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

class Teacher(SchoolMember):
    salary = 0
    def __init__(self, name, age, salary): #하나는내껀데 다른건 부모클래스에게 전달
        super().__init__(name, age)
        self.salary = salary
