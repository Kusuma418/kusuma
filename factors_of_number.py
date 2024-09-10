#factors of a number
def factors(n):
    i=1
    while(i<=n):
        if(n%i==0):
            print(i,"is factor",n)
        i+=1
factors(6) #example
