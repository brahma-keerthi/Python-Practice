# class Num:        #Declaration of class #No memory will be allocated at this time
#     def sum(self):
#         return self.a + self.b

# Add = Num()  #Creation of the object to a valid class
# Add.a= 3
# Add.b = 5
# s = Add.sum()
# print(s)

# class RaliwayForm:
#     formName = "Railway Form"
#     def printData(self):
#         print(f"Name of the passanger is {self.name}")
#         print(f"Name of the train is {self.train}")

# HarryForm = RaliwayForm()
# HarryForm.name = "Harry"
# HarryForm.train = "Rajdhani Express"
# HarryForm.printData()

# class Employee:
#     company = "google"

# Harry = Employee()     #Class Attributes
# Rohan = Employee()
# print(Harry.company)
# Rohan.company = "Microsoft"     #Instance Attributes  
# print(Rohan.company)     #Instance Attributes has high priority over Class Attributes

# class Add:
#     def sum(self):
#         print("Sum is", self.a + self.b)

# Addition = Add()
# Addition.a = 3
# Addition.b = 7
# Addition.sum()   #is equivalent to Add.sum(Addition)
# # the self is used as the argument

# Extra Argument along with the self
# class Winner:
#     def greet(self, sign):
#         print(self.name , "is the winner\n", sign )

# Rohan = Winner()
# Rohan.name = "Rohan"
# Rohan.greet("Sachin")  #This is an extra argument which can be given along with self



# Sometimes we need not need the self as the Argument
class Employee:
    @staticmethod  # this we not allow self argument by default and we can add the argument if we want
    def greet(name): #Static method is used when the object is not required
        print("Good morning,", name)

Benne = Employee()
Benne.greet("Pratheek")  #@staticmethod is called as the decorator which which is a function itself and will alter the other function