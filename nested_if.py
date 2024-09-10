#nested if
char=input()
if((char >= "A" and char <="Z") or (char >= "a" and char <= "z")):
    if(char >= "A" and char <= "Z"):
        print("Upperacse Aplhabet")
    else:
        print("Lowercase Alphabet")
else:
    print("Not a Alphabet")

