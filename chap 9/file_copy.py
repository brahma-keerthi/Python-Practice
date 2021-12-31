#This program will create the copy of the file this text 

with open("this.txt", 'r') as f:
    text = f.read()

name = input("Enter the name of the new file in which the copy has to be made: ")
with open(name, 'w') as f:
    f.write(text)