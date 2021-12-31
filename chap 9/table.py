#This program will generate the tables from 2 to 20 in different folder

for i in range(2, 21):
    g = open(f"Tables//Table{i}.txt", "w")

    g.write("This is multiplication table of " + str(i))
    for j in range(1 , 11):
        mul = j*i
        g.write(f"\n{i} * {j} = {mul}")

    g.close()