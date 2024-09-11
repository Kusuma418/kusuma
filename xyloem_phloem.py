#Xyleom Number or Phloem Number
def XyleomPhloem():
    num=int(input("enter a number:"))
    sum1=num%10
    num//=10
    sum2=0
    while(num>9):
        ld=num%10
        sum2+=ld
        num//=10
    sum1+=num
    if(sum1==sum2):
        print("given number is Xyloem Number")
    else:
        print("given number is Phloem Number")
XyleomPhloem()
    
    
