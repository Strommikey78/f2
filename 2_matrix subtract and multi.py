m1=[]
r1=int(input("enter number of row for m1: "))
c1=int(input("enter number of columns for m1: "))
m2=[]
r2=int(input("enter number of row for m2: "))
c2=int(input("enter number of columns for m2: "))
m3=[]
m4=[]
if(r1==r2 and c1==c2 and c1==r2) :
    for i in range(r1) :
        a=[]
        for j in range(c1) :
            a.append(int(input("Enter elements for m1: ")))
        m1.append(a)
    for i in range (r2) :
        b=[]
        for j in range(c2) :
            b.append(int(input("Enter elements for m2: ")))
        m2.append(b)
    for m1r in m1 :
        print(m1r)
    for m2r in m2 :
        print(m2r)
    for i in range(r1) :
        c=[]
        for j in range(r2) :
            c.append(m1[i][j]-m2[i][j])
        m3.append(c)
    for m3r in m3 :
        print(m3r)
    for i in range(r1) :
        d=[]
        for j in range(r2) :
            d.append(0)
        m4.append(d)
    for i in range(r1) :
        for j in range(c2) :
            for k in range(c1) :
                m4[i][j]+=m1[i][k]*m2[k][j]
    for m4r in m4 :
        print(m4r)