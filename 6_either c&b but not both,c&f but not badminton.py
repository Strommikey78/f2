Cricket=list(input("Enter students interested for Cricket: ").split(", "))
Badminton=list(input("Enter students interested for Badminton: ").split(", "))
Football=list(input("Enter students interested for Football: ").split(", "))

#list of students who play either cricket or badminton but not both
def eit_or() :
    temp=[]
    for students in Badminton :
        if students not in Cricket :
            temp.append(students)
    for students in Cricket :
        if students not in Badminton :
            temp.append(students)
    print("list of students who play either cricket or badminton but not both: ",temp)
eit_or()

#list of students who play Cricket and Football but not Badminton    
def and_but() :
    temp=[]
    for students in Cricket :
        if students in Football and students not in Badminton :
            temp.append(students)
    print("list of students who play Cricket and Football but not Badminton: ",temp)
and_but()