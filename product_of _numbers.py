#product of numbers from 1 to 10
def ProdOfSeries(n):
    prod=1
    i=1
    while(i<=n):
        prod*=i
        i+=1
    print(prod) #return prod
ProdOfSeries(10) #example 
