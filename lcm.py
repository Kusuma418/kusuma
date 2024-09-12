#LCM(least common multiple) of two numbers
def LCM():
    n1=int(input("enter a number1:"))
    n2=int(input("enter a number2:"))
    i=1
    while(True):
        if((n1*i)%n2==0):
            print((n1*i),"is lcm of",n1,"and",n2)
            break
        i+=1
LCM()

