#Proper factors of a number
#proper factors are the factors which does not include gievn number 
def properfactors(n):
    i=1
    while(i<n):
        if(n%i==0):
            print(i,"is factor",n)
        i+=1
properfactors(6) #example
