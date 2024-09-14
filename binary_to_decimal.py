#binary to decimal
def bin_to_dec():
    num=int(input("enter a number:"))
    base=1
    result=0
    while(num!=0):
        rem=num%10
        result=result+(rem*base)
        base=base*2
        num//=10
    print(result)
bin_to_dec()
