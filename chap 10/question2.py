# will create a class calculator will find out sq, cube and sqrt of a number

# class Calci:
#     @staticmethod
#     def greet():
#         print("Hello user use my Calcutator")
#     def sq(self):
#         return self.a*self.a     #adding a semicolon does not give error in return statement

#     def cube(self):
#         return self.a*self.a*self.a

#     def sqrt(self):
#         return self.a**0.5

# Num = Calci()
# Num.greet()
# Num.a = int(input("Enter the number: "))
# print("Sq is", Num.sq())
# print("Cube is", Num.cube())
# print("Sqrt is", Num.sqrt())

class Num:
    def __init__(self, num):
        self.number = num

    def sq(self):
        print("Sq is", self.number**2)

    def sqrt(self):
        print("Sqrt is", self.number**0.5)

    def cube(self):
        print("Cube is", self.number**3)

a = Num(int(input("Enter the number: ")))
a.sq()
a.sqrt()
a.cube()
