#Twisted prime also known as Emirp Number
def emirp():
    num=int(input("enter a number:"))
    c=0
    for i in range(1,num+1):
        if(num%i==0):
            c+=1
    if(c!=2):
        print("given number is not prime and cannot be twisted")
    else:
        rev=0
        while(num!=0):
            ld=num%10
            rev=rev*10+ld
            num//=10
        count=0
        for i in range(1,rev+1):
            if(rev%i==0):
                count+=1
        if(count==2):
            print("given number is emirp number")
        else:
            print("given number is not a emirp number")
emirp()


