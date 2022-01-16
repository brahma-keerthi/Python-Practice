class Emp:
    salary = 85894

    def changesalary(self, salary):
        self.salary = salary
        return salary

    @classmethod   #this method will access the class attributes
    def changeSalary(cls, salary):
        cls.salary = salary
        return salary



e = Emp()
print(e.salary)

print(e.changesalary(254))  # this will change the instance attribute
print(e.salary)

print(e.changeSalary(659845)) #this will change class attributes
print(e.salary)