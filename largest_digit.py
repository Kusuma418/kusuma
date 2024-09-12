#largest digit from given number
def largest():
    num=int(input("enter a number:"))
    lar=0
    while(num!=0):
        last_digit=num%10
        if(last_digit > lar):
            lar=last_digit
        num//=10
    print(lar,"is the largset from given number")
largest()
