# This program will create a hindi dictionary and will give the user to access it

hindi = { "Bahar" : "Out", "Uper":"Up", "Neeche":"Down"}
print("The given dictionary contains", hindi.keys())
a = input("Enter the Word whose meaning has to be accessed: ")
print("The meaning of the word", a, "is", hindi[a])