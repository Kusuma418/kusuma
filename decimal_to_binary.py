#decimal to binary
def dec_to_bin():
    num=int(input("enter a number:"))
    base=1
    result=0
    while(num!=0):
        rem=num%2
        result=result+(rem*base)
        base=base*10
        num//=2
    print(result)
dec_to_bin()
