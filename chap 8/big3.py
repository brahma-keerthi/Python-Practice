#This program will give the biggest of the 3 numbers

def big(a, b, c):
    if(a>b and a>c):
        return a

    elif(b>a and b>c):
        return b

    elif(c>a and c>b):
        return c

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

print(f"The biggest amoung {a}, {b} and {c} is {big(a,b,c)}")