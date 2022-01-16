class string:
    def __init__(self, a):
        self.a = a

    # def __repr__(self):
    #     return self.a

    def __add__(self, b):
        return self.a + b

    def __mul__(self, c):
        return self.a + c

str = string("Benne")
print(str + " ge illa Tunne")
print(str * " hengsu")