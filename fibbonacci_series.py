#Fibbonacci Series from 1 to 10
def fibbo():
    n=int(input("enter a range:"))
    a=0
    b=1
    sum=0
    for i in range(1,n+1):
        print(sum,end=' ')
        a=b
        b=sum
        sum=a+b
fibbo()
        
    
    
