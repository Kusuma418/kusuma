#Strong Number
def StrongNum():
    num=int(input("enter a digit:"))
    sum=0
    temp=num
    while(num!=0):
        ld=num%10
        fact=1
        i=1
        while(i<=ld):
            fact=fact*i
            i+=1
        sum+=fact
        num//=10
    if(sum==temp):
        print(temp,"is a Strong Number")
    else:
        print(temp,"is not a Strong Number")
StrongNum()
    
