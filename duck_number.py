#Duck Number
def DuckNum():
    num=int(input("enter a number:"))
    prod=1
    while(num!=0):
        ld=num%10
        prod*=ld
        num//=10
    if(prod==0):
        print("Given number is duck number")
    else:
        print("Given number is not a duck number")
DuckNum()
    
    
