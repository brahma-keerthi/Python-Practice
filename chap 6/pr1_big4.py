# This program will find the biggest of the four numbers in the given numbers

a = [ int(input("Enter the first number: ")), int(input("Enter the second number: ")),
    int(input("Enter the third number: ")), int(input("Enter the fourth number: "))]

if(a[0]>a[1] and a[0]>a[2] and a[0]>a[3]):
    print(a[0], "is Biggest")

elif(a[1]>a[0] and a[1]>a[2] and a[1]>a[3]):
    print(a[1], "is Biggest")

elif(a[2]>a[0] and a[2]>a[1] and a[2]>a[3]):
    print(a[2], "is Biggest")

elif(a[3]>a[0] and a[3]>a[1] and a[3]>a[2]):
    print(a[3], "is Biggest")