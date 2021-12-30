# This program will convert the cm to inch

def con(a):
    return a*0.393

a = int(input("Enter the lenght in centi meters: "))
print(a, "cms =", con(a), "inch")
    