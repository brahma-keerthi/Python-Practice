# This program will replace the word donkey by ######

#f = open("donkey.txt", 'r')
#text = f.read()
text = input("Enter the sentence: ")
print("Before the Process\n", text)
text = text.lower()
text = text.replace("donkey", "#@!$%^")
#f.close()

f = open("donkey.txt", 'w')
f.write(text)
f.close

print("After the Process\n", text)