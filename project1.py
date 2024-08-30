#number guessing
import random
import math
lower = int(input("enter a lower boundary:"))
upper = int(input("enter a upper boundary:"))
x = random.randint(lower, upper)
total_chances = math.ceil(math.log(upper - lower + 1, 2))
print("you have only",total_chances,"for guessing a number")
count = 0
flag = False
while count < total_chances:
    guess = int(input("enter a number:"))
    count+=1
    if(x == guess):
        print("congratulations! you guessed correct")
        flag = True
        break
    elif(guess > x):
        print("oh you guessed too high")
    elif(guess < x):
        print("ohh you guessed too low")
if not flag:
    print("Betterluck next time")
    
        
        
