greet = '''Dear <name>,
        You have been selected...
        <date>'''
name = input("Enter the Name: ")
date = input("Enter the Date: ")

greet = greet.replace("<name>", name)
greet = greet.replace("<date>", date)

print(greet)