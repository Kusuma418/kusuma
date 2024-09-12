#GCD(greatest common divisor) of two numbers
def GCD():
    n1=int(input("enter a number1:"))
    n2=int(input("enter a number2:"))
    i=1
    gcd=1
    while(i<=n1 and i<=n2):
        if(n1%i==0 and n2%i==0):
            gcd=i
        i+=1
    print(gcd,"is gcd of",n1,"and",n2)
GCD()
