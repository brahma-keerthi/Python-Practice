# This program convert cel to farenheit

def con(c):
    f = c*1.8 + 32
    return f

c = float(input("Enter the temperature in celcius: "))
print(c, "celcius =", con(c), "fahenheit")