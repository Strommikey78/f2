s=[]
x=int(input("Enter roll number of students who attended training program: "))
for i in range(len(x)) :
    y=int(input ("enter roll number: "))
    s.append(y) 
s.sort()
l=len(s)
def senti_search() :
    x=int(input("Enter roll number of students to be search: "))
    last=s[l-1]
    s[l-1]=x
    i=0
    while(s[i]!=x) :
        i+=1
    s[l-1]=last
    if (i<l-1 or s[l-1]==x) :
        print(x," found!") 
    else :
        print(x," not found!")
senti_search() 

def fib_search() :

"""--------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------
 incomplete incomplete incomplete incomplete incomplete incomplete incomplete incomplete 
-----------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------"""