print("WELCOME TO THE COMMUNITY PARTY... ")
data=int(input("IF YOU ARE THE MEMBER OF THIS COMMUNITY WRITE '1'...OTHERWISE WRITE ANY NUMBER..."))
bill=0
if data==1:
    age = int(input("enter you age.."))
    print("welcome to the party!")
    if age<=12:
        bill = 10
        print("Child ticket costs $5 ")
    elif age<=18:
        bill = 15
        print("Teenager ticket costs $10")
    else :
        bill = 20
        print("Adult ticket costs $15")

    card=input("if you want to get VIP pass write y for yes and n for no")
    if card =="y":
       print(f"your total bill ${bill}")

else :
    print("sorry,You can't enter the party , cuz you are not the member of the community.")
