#simple calculator using functions

def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return abs(num1-num2) # abs() returns absolute value
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1//num2

num1=int(input("enter a value1:"))
num2=int(input("enter a value2:"))

print("enter your choice \n 1-Addition \n 2-Subraction \n 3-Multiplication \n 4-Division \n")
user_oper=int(input("select your choices from 1,2,3,4 :"))
while not(user_oper>=1 and user_oper<=4):
    print("enter a valid number")
    user_oper=int(input("select your choices from 1,2,3,4 :"))
if(user_oper==1):
    print(num1,"+",num2,"=",add(num1,num2))
elif(user_oper==2):
    print(num1,"-",num2,"=",sub(num1,num2))
elif(user_oper==3):
    print(num1,"*",num2,"=",mul(num1,num2))
else:
    print(num1,"//",num2,"=",div(num1,num2))
    

    
    
