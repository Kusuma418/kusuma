#SPY Number
#if sum of digits is equal to prod of digits then the given number is  known as SPY number
def SPYnumber(num):
    sum=0
    prod=1
    while(num!=0):
        last_digit=num%10#extract last digit from given number
        sum+=last_digit
        prod*=last_digit
        num//=10  #remove last digit from given number
    if(sum==prod):
        print("SPY number")
    else:
        print("not a SPY number")
SPYnumber() #pass a data

