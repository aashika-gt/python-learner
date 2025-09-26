#python pizza
print("Welcome to Python Pizza Deliveries!")
bill=0
size = input("What size pizza do you want? S, M or L: ")
if size=="S":
   print("Small pizza costs(S):$15")
   bill+= 15
elif size=="M":
    print("medium pizza costs(S):$20")
    bill+= 20
elif size=="L":
    print("large pizza costs(S):$25")
    bill += 25
else:
    print("sorry, you've typed something wrong")

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni=="Y":
    if size=="S":
      bill +=2
    else:
      bill +=3

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese =="Y":
      bill+=1
print(f"your final bill is: ${bill}.")

