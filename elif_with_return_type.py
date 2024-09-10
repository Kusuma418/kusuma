#elif with return type
def pos_neg(num):
    if(num>0):
        return "Postive Number"
    elif(num<0):
        return "Negative Number"
    return "Neutral Number"
print(pos_neg(0)) # example data pass while calling function
