#Palindrome Number 
def rev(num):
    rev=0
    temp=num
    while(num!=0):
        last_digit=num%10
        rev=rev*10+last_digit
        num//=10
    if(temp==rev):
        print(temp,"is palindrome number")
    else:
        print(temp,"is not palindrome number")  
rev() 
