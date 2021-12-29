# This program will determine whether the given program is spam or not

s = input("Give the sentence: ")

if(s.find("make a lot of money")>=0 or s.find("buy now")>=0 or s.find("subscribe this")>=0 or s.find("click this")>=0):
    print("!!!!! SPAM !!!!!")

else:
    print("NOT SPAM")