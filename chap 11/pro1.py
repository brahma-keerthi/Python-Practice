class Employee:
    increment = 0.02

    @property
    def totalSalary(self, salary):
        return salary + salary*self.increment

    @totalSalary.setter
    def totalSalary(self):
        return (self.totalSalary - self.salary)/self.salary

e = Employee().totalSalary(2000)
print(e.totalSalary)