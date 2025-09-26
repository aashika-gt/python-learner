print("WELCOME TO THE COMMUNITY PARTY... ")
data=int(input("IF YOU ARE THE MEMBER OF THIS COMMUNITY WRITE '1'...OTHERWISE WRITE ANY NUMBER..."))
if data==1:
    age = int(input("enter you age.."))
    print("welcome to the party!")
    if age<=12:
        print("your ticket costs $5 Thank You")
    elif age<=18:
        print("your ticket costs $10")
    else :
        print("your ticket costs $15")
else :
    print("sorry,You can't enter the party , cuz you are not the member of the community.")
