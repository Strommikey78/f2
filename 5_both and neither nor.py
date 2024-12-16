Cricket = list(input("Enter students interested in Cricket: ").split(", "))
Badminton = list(input("Enter students interested in Badminton: ").split(", "))
Football = list(input("Enter students interested in Football: ").split(", "))

# List of students who play both cricket and badminton
def both():
    both = []
    for student in Badminton:
        if student in Cricket:
            both.append(student)
    print("List of students who play both cricket and badminton:", both)
both()

# List of students who play neither cricket nor badminton
def nei():
    neither = []
    for student in Football:
        if student not in Cricket and student not in Badminton:
            neither.append(student)
    print("List of students who play neither cricket nor badminton:", neither)
nei()

