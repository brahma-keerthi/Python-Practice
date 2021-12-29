# This program will intake the marks of the student and will give it in sorted manner

list = []

for i in range(0, 6):
    list.insert(i, int(input("Enter the marks of student: ")))

list.sort()  #this will sort the list
print(list)


