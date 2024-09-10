#Prime Number
#a number which is divisible by 1 and itself then it is known as prime number
def PrimeNumber(n):
    count=0
    i=1
    while(i<=n):
        if(n%i==0):
            count+=1
        i+=1
    if(count==2):
        print(n,"is prime number")
    else:
        print(n,"is not a prime number")
PrimeNumber(7) #example
