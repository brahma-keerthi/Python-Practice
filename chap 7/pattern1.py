'''This program will print the pattern
           *
          ***
         *****
        *******'''
    
n = int(input("Enter the number of lines: "))

for i in range(0,n):
    print((" "*(n-i-1)) + ("*"*(i+1)) + ("*"*(i)))