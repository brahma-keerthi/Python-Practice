#This program will tell whether the student is pass or fail

marks = [ int(input("Enter the marks of sub1: ")), int(input("Enter the marks of sub2: ")),
                        int(input("Enter the marks of sub3: "))]

total = (marks[0]+marks[1]+marks[2])/3

if(marks[0]<33 or marks[1]<33 or marks[2]<33 or total<40 ):
    print("The student is FAIL")

else:
    print("The student is PASS with", total,"% of marks")

