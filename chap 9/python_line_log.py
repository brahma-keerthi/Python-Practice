#This program will tell in which line the word python is present

f = open("log.txt")
text = f.readline()

i = 1
while(text != ""):
    if("python" in text.lower()):
        print("PRESENT in line", i)
        exit(0)
        
    i = i+1
    
    text = f.readline()
else:
    print("ABSENT")

f.close()