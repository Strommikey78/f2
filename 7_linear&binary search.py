#linear and binary search--------
s=[]
x=int(input("Enter roll number of students who attended training progam: "))
for i in range(x) :
    y=int(input("enter roll number: "))
    s.append(y)
def linear_search() :
    f=0
    x=int(input("Enter roll number to be search: "))
    for i in range(len(s)) :
        if (s[i]==x) :
            print(x, "found!")
            f=0
    if(f!=0) :
        print(x, "not found!")
def binary_search() :
    f=0
    low=0
    high=len(s)-1
    x=int(input("Enter roll number to be search: "))
    while(low<=high) :
        mid=(high+low)//2
        if (x==s[mid]) :
            print(x, "Found!")
            f+=1
        if (x<s[mid]) :
            high=mid-1
        else :
            low=mid+1
    if(f==0) :
        print(x,"not found!")
linear_search()
binary_search()

