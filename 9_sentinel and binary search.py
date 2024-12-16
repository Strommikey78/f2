s=[]
x=int(input("Enter number of students who attended training programs: "))
for i in range(x) :
    y=int(input("Enter roll number: "))
    s.append(y)
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

def binary_search() :
    f=0
    low=0
    high=len(s)-1
    x=int(input("Enter roll number of student to be search: "))
    while(low<=high) :
        mid=(high+low)//2
        if(s[mid]==x) :
            print(x," found!")
            f+=1
        if(s[mid]>x) :
            high=mid-1
        else :
            low=mid+1
    if(f==0) :
        print(x,"not found!")
binary_search() 



