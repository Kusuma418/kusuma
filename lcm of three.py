#LCM(least common multiple) of three numbers
def LCM():
    n1=int(input("enter a number1:"))
    n2=int(input("enter a number2:"))
    n3=int(input("enter a number3:"))
    i=1
    while(True):
        if(i%n1==0 and i%n2==0 and i%n3==0):
            print(i,"is lcm of",n1,n2,"and",n3)
            break
        i+=1
LCM()

