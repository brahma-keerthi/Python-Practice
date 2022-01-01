# This program will give us an idea about the __init__ function

class Employee:
    def __init__(self, name, company, EmpID):  #This function does not require any call to run
        print("This constructor function will run even when this function is not called")
        self.name = name
        self.company = company
        self.EmpID = EmpID

    def printDetails(self):
        print("The name of employee is", self.name)
        print("The name of the company is", self.company)
        print("The Employee ID is", self.EmpID)

Harry = Employee("Harry", "Google", 5266)  #This is a new way to create the object
Harry.printDetails()
