# This program will tell whether the given username will contain less than ten characters or not

s = input("Enter the username: ")

if(len(s)<10):
    print("Given username contains less than 10 characters")

else:
    print("Given username contains 10 or more characters")