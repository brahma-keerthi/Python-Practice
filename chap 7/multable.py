# This program will print the multiplication table of a givne number

n = int(input("Enter the number: "))

print("The multiplication table of", n)
#for i in range(0,10):
i=0
while i<10:
    mul = (i+1)*n
    print(n,"*",i+1,"=", mul)
    i=i+1