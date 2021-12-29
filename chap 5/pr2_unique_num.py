# This program will ask to input the 8 numbers and will display the unique numbers

a = set()
for i in range(0,8):
    a.add(int(input("Enter the number: ")))

print("The unique numbers entered are: ",a)