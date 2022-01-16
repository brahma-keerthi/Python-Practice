class Add:
    def __init__(self, a):
        self.a = a

    def __repr__(self):
        return self.a

    def __add__(self, b):
        c = self.a*b
        return c

a = Add(5)
print(a + 9) #returns the multiplied value