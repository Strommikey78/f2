s=input("Enter a string: ")

#to check whether given string in palindrome
def palindrome() :
    x=s[::-1]
    if (s==x) :
        print("string is palindrome!")
    else :
        print("String is not palindrome!!")
palindrome()

#to count occurence of each word in string 
def occurence() :
    c=0
    x=s.split()
    w=input("Enter word: ")
    for i in range (len(x)) :
        if (x[i]==w) :
            c+=1
    print(w," word occured ",c," times in a string.")
occurence()
