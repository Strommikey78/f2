m1=[]
r1=int(input("Enter number of rows in m1: "))
c1=int(input("Enter number of columnss in m1: "))
m2=[]
r2=int(input("Enter number of rows in m2: "))
c2=int(input("Enter number of columnss in m2: "))
m3=[]
tp=[]
if (r1==r2 and c1==c2) :
    for i in range(r1) :
        a=[]
        for j in range(c1) :
            a.append(int(input("Enter elements for m1 : ")))
        m1.append(a)
    for i in range(r2) :
        b=[]
        for j in range(c2) :
            b.append(int(input("Enter elements for m2 : ")))
        m2.append(b)
    for m1r in m1 :
        print(m1r)
    for m2r in m2 :
        print(m2r)
    for i in range(r1) :
        c=[]
        for j in range(c1) :
            c.append(m1[i][j] + m2[i][j])
        m3.append(c)
    print("addition of 2 matrices :")
    for m3r in m3 :
        print(m3r)

    for i in range(c1) :
        d=[]
        for j in range(r1) :
            d.append(0)
        tp.append(d)
    for i in range(c1) :
        for j in range(r1) :
            tp[j][i]=m1[i][j]
    print("transpose matrix is :")
    for tpr in tp :
        print(tpr)


            