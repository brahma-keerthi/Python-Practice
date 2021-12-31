#This program will tell whether the given log file contains the python or not

with open("log.txt", 'r') as f:
    text = f.read()
    text = text.lower()

if "python" in text:
    print("PRESENT")
else:
    print("ABSENT")