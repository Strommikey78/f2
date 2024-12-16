s=[]
x=int(input("Enter roll number of students who attended training program: "))
for i in range(len(x)) :
    y=int(input ("enter roll number: "))
    s.append(y) 
s.sort()
def linear_search() :
    f=0
    n=int(input("Enter roll number of student to be search: "))
    for i in range (len(s)) :
        if (s[i]==n) :
            print(n, "found!") 
            f=0
    if (f!=0) :
        print(n, " not found!")
def fib_search() :

"""--------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------
 incomplete incomplete incomplete incomplete incomplete incomplete incomplete incomplete 
-----------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------"""