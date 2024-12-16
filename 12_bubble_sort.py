arr=[]
x=int(input("Enter number of first year students: "))
for i in range(x) :
    y=float(input("Enter percentage: "))
    arr.append(y)
l=len(arr)

def bubble_sort() :
    for i in range(l) :
        for j in range(0,l-i-1) :
            if (arr[j]>arr[j+1]) :
                arr[j],arr[j+1]=arr[j+1],arr[j]
    print(arr)
bubble_sort()

#top five scores 
if(l>=5) :
    Top_five_scores=arr[-5:] 
    print("Top five scores: ",Top_five_scores)
else :
    print("number of students in first year is less than 5")
    