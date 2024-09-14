#neon number
def neon_num():
    num=int(input("enter a numner:"))
    sum=0
    sq=num**2
    while(sq!=0):
        sq_ld=sq%10
        sum=sum+sq_ld
        sq//=10
    if(sum==num):
        print("given number is neon number")
    else:
        print("given number is not a neon number")
neon_num()
