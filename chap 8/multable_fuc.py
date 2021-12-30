# This program will print the multiplication table 

def mul(n):
    for i in range(10):
        mul = n * (i+1)
        print(f"{n} * {i+1} = {mul}")

n = int(input("Enter the number whose multiplication has to be printed: "))
mul(n)