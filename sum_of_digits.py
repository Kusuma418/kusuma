#sum of digits from a given number
def SumofDigits(num):
    sum=0
    while(num!=0):
        last_digit=num%10
        sum+=last_digit
        num//=10
    print(sum)  #return sum

