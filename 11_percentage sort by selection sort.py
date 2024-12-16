arr=[]
x=int(input("Enter number of first year students: "))
for i in range(x) :
    y=float(input("Enter percentage: "))
    arr.append(y)
l=len(arr)

def selection_sort() :
    for i in range(l) :
        ind=i
        small=arr[i]
        for j in range(i+1,l) :
            if (small>arr[j]) :
                small=arr[j]
                ind=j
        arr[i],arr[ind]=arr[ind],arr[i]
    print(arr)
selection_sort()
#top five scores
if (l>=5) :
    top_five_scores=arr[-5:]
    print("Top 5 scores: ",top_five_scores)
else :
    print("number of students in first year is less than 5")

