arr=[]
x=int(input("Enter number of first year students: "))
for i in range(x) :
    y=float(input("Enter percentage: "))
    arr.append(y)
l=len(arr)

low=0
high=l-1
def partition(arr,low,high) :
    i=low-1
    pivot=arr[high]
    for j in range(low,high) :
        if (arr[j]>=pivot) :
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

def quick_sort(arr,low,high) :
    if (low<high) :
        pi=partition(arr,low,high)
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)

quick_sort(arr,0,l-1) 
print(arr)
    
#top five scores
if(l>=5) :
    Top_five_scores=arr[:5] 
    print("Top five scores: ",Top_five_scores)
else :
    print("number of students in first year is less than 5")
