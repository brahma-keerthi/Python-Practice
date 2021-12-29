# This program will take the name of as key and language as the values

s ={}

for i in range(0,4):
    s[input("Enter the name of the person: ")] = input("Enter the language name: ")

print(s)

# if the key is same, the value to following key will be updated itself as a dic can contain only one key name
# but same value could be present in different keys