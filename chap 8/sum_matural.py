# This program will give the sum of the first n natural numbers by recurssion

def sum(a):
    if(a==1):
        return 1

    s = a + sum(a-1)
    return s

a = int(input("Enter the number upto which the sum has to be calculated: "))
print("The sum of first", a, "natural numbers is", sum(a))