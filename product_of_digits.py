#product of digits from a given number
def prodofDigits(num):
    prod=1
    while(num!=0):
        last_digit=num%10 #extract last digit from given number
        prod*=last_digit
        num//=10  #remove last digit from given number
    print(prod)  #return prod

