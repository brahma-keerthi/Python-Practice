# This program will tell whether the given letter contains harry or not

s = (input("Enter the text: "))
s = s.lower() # converts entire string small case

if s.find("harry")==-1:
    print("This text does not refer to Harry")

else:
    print("This text is referring to Harry")