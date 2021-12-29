# this program will add the items of the list and display the sum;

list = []
sum =0

for i in range(0, 4):
    list.insert(i, int(input("Enter the integer value: ")))
    sum = sum + list[i]
    
print(list)
print("The sum of all elements of a list is", sum)