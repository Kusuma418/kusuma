#smallest digit from given number
def smallest():
    num=int(input("enter a number:"))
    small=9
    while(num!=0):
        last_digit=num%10
        if(last_digit < small):
            small=last_digit
        num//=10
    print(small,"is the smallest from given number")
smallest()
