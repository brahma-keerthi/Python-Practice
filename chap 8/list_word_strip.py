# This program will remove the word and will strip the list 

def strip(l, word):
    l = l.remove(word)
    return l

l = []

n = int(input("Enter the number of elements in list: "))
for i in range(0, n):
    l[i] = (input("Enter the words in list "))

word = input("Enter the word which has to be removed and has to be striped: ")

print("After stripping: \n", strip(list, word))
