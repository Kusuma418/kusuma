#match case example
num=int(input("enter a number:"))
match num:
    case x if x>0:
        print("Postive Number")
    case y if y<0:
        print("Negative Number")
    case _ :
        print("Zero")


