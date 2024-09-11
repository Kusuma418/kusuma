#Armstrong Number
def Armstrong():
    num=int(input("enter a number:"))
    count=0
    temp=num
    while(temp!=0):
        count+=1
        temp//=10
    temp1=num
    sum=0
    while(temp1!=0):
        ld=temp1%10
        i=1
        prod=1
        while(i<=count):
            prod=prod*ld
            i+=1
        sum=sum+prod
        temp1//=10
    if(sum==num):
        print(num,"is a armstrong number")
    else:
        print(num," is not a armstrong number")
Armstrong()

    
    
