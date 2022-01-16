class Animals:
    def __init__(self):
        print("This is a animal")
        print("Lives in jungle")

    def type(self):
        print("Wild animals")

    def sound(self):
        print("Makes sound")

    def move(self):
        print("Can run... ")

class Pets(Animals):
    def __init__(self):
        print("This is a pet")
        print("Lives in Home")

    def type(self):
        print("pet animal")

    def sound(self):
        super().sound()
    
    def move(self):
        super().move()

class Dogs(Pets):
    def __init__(self):
        print("This is a Pet Dog")
        super().__init__()

    def type(self):
        super().type()

    def sound(self):
        print("Bow, Bow...")

    def move(self): 
        super().move()

    def legs(self):
        print("4 legs")

animal = Animals()
animal.type()
animal.sound()
animal.move()

pet = Pets()
pet.type()
pet.sound()
pet.move()

dog = Dogs()
dog.type()
dog.sound()
dog.move()
dog.legs()

