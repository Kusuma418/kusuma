#reverse a number
def rev(num):
    rev=0
    while(num!=0):
        last_digit=num%10
        rev=rev*10+last_digit
        num//=10
    print(rev)
rev(232) #example usage
