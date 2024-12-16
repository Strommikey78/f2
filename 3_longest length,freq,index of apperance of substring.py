# a)  To display word with the longest length
s=input("Enter a string: ")
def longest_length(s) :
    maxi=0
    x=s.split()
    for i in range(len(x)) :
        if (len(x[i])>maxi) :
            maxi=len(x[i])
            strin=x[i]
    print("longest word is: ",strin," with length:",maxi)
longest_length(s)

# b)  To determines the frequency of occurrence of particular character in the string
def occurence() :
    c=0
    x=input("Enter the character : ")
    for i in s:
        if (x==i) :
            c+=1
    print(x," character occured in string ",c," times.")
occurence()

# c) To display index of first appearance of the substring
def sub() :
    sub=input("Enter the substring : ")
    for i in range(len(s)) :
        if (s[i:i+len(sub)]==sub) :
            x=i
    print ("substring appear at index ", x)
sub()
