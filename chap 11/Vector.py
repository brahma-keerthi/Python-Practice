class Vec2d:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print(self):
        print("The given 2-d vector is>> ")
        print(f"{self.a}i + {self.b}j")

class Vec3d(Vec2d):
    def __init__(self,a, b, c):
        super().__init__( a, b)
        self.c = c

    def print(self):
        print("The given 3-d vector is>> ")
        print(f"{self.a}i + {self.b}j + {self.c}k")

v2 = Vec2d(3, 6)
v2.print()

v3 = Vec3d(9, 1, 8)
v3.print()
