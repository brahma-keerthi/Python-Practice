# This program will print the pattern 

n = int(input("Enter the number: "))

for i in range(n):
    if ( i==0 or i==n-1):
        print("*"*n)
    else:
        print("*" + " "*(n-2) + "*")