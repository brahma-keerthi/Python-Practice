## super() 

class Man:
    def speak(self):
        print("I m speaking...")

class Employee(Man):
    def work(self):
        super().speak()
        print("I am working")

class Programmer(Employee):
    def code(self):
        super().work()
        print("I am coding ")

m = Man()
m.speak()
print()

e = Employee()
e.work()
print()

p = Programmer()
p.code()
