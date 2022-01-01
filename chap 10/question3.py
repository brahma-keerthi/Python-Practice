class Num:
    a = 89
    print("value of a in class attribute", a)

New = Num()
New.a = 0
print("value of a in object attribute", New.a)