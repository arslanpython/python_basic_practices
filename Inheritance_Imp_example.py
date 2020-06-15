class Person:
    num = []

    def printname(self):
        self.num.append(20)


class Student(Person):
    num = [10]

    def __init__(self):
        self.printname()
        print('Student list -> ', self.num)

    print(num)


class Employee(Person):
    num = []

    def __init__(self):
        self.printname()
        print('Employees list -> ', self.num)

    print(num)


p = Student()
e = Employee()
