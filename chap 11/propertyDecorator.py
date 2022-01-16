# This will give the property decorator

class Employee:
    company = "Benne"
    salary = 65200
    salaryBonus = 5000

    # totalSalary = salary + salaryBonus  #This also works as same as decorator 

    @property
    def totalSalary(self):
        return self.salary + self.salaryBonus

    @totalSalary.setter
    def totalSalary(self):
        return self.salary + self.salaryBonus

e = Employee()
print(e.totalSalary)

e.salaryBonus = 500
print(e.totalSalary)

