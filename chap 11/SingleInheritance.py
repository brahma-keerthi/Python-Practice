class Employee:
    company = "Google"

    def getDetails(self):
        print(f"The company is {self.company}")

class FamilyMan:
    company = "Family"

    def printDetails(self):
        print(f"The company is {self.company}")

# class Programmer(Employee):
#     language = "Python"
#     company = "Microsoft"  #local attribute has more preference than class attributes

#     def printDetails(self):
#         print(f"Coding language is {self.language}")

# e = Employee()
# e.getDetails()
# p = Programmer()
# p.printDetails()
# p.getDetails()

class Man(FamilyMan, Employee):  #family man has higher order of precedence
    def __init__(self):
        print("This is double inherited class")

g = Man()
print(g.company)
