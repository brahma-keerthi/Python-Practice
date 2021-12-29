# This program will find the factorial of the number

n = int(input("Enter the number: "))

fac=1
for i in range(1,n+1):
    fac = fac * i

print("Factorial of", n, "is", fac)