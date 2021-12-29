#This program will intake the lists of 7 fruits 
list=[]
for i in range(0, 7):
    list.insert(i, input("Enter the name of the fruit:"))

print(list)
print(type(list))