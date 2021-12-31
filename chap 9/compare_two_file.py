# This program will compare the two files and tells whether it is identical or not

file1 = input("Enter the name of the file1: ")
file2 = input("Enter the name of the file2: ")

with open(file1) as f:
    text1 = f.read()
with open(file2) as g:
    text2 = g.read()

if(text1 == text2):
    print("IDENTICAL")
    print("Both contain>>\n", text1)

else:
    print("NOT IDENTICAL")
    print(file1, "contains\n", text1, "\n\n")
    print(file2, "contains\n", text2)