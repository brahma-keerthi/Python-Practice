# This program will wipe out the contents of the file choosen

name = input("Enter the name of the files: ")

with open(name, 'w') as f:
    f.write("")