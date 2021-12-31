f = open("poems.txt", "r")
text = f.read()
text = text.lower()
n = text.find("twinkle")
#print(n)
if(n > 1):
    print("PRESENT")
else:
    print("Absent")

print(text)
f.close()