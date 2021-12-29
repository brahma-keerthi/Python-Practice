s = set()   #empty set
print(len(s))

s.add(20)
print(len(s))

s.add(20.0)  #20 and 20.0 are the same in py
print(len(s))

s.add("20")
print(len(s))