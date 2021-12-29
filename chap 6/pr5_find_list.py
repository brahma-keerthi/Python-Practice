# This program will tell whether the given name is present in the given list

s = [ "benne", "prathi","pratheek", "gandu", "lowde"]

name = input("Enter the name: ")

if(s.count(name) == 0):
    print(name, "is not present in the list")

else:
    print(name, "is present in the list")