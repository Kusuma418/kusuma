#Perfect Number
#if the sum of proper factors is equal to given number then it is known as perfect number
def PerfectNumber(n):
    sum=0
    i=1
    while(i<n):
        if(n%i==0):
            sum+=i
        i+=1
    if(sum==n):
        print(n,"is perfect number")
    else:
        print(n,"is not a perfect number")
PerfectNumber(3) #example
