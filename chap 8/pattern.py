# this program will create a patrean usin greccussion

def pat(a):
    if(a == 0):
        exit(0)

    print("*"*a)
    pat(a-1)

a = int(input("Eneter the number of lines the pattern has to be printed: "))
pat(a)