import random
print("Wanna play Rock ,Paper ,Scissor")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice=input("What do you want to choose? write '0' for rocks '1' for paper and '2' for scissors")
if choice=="0":
    print(rock+"\nYour choice is : ROCKS")
elif choice=="1":
    print(paper+"\nYour choice is : PAPER")
elif choice=="2":
    print(scissors+"\nYour choice is : SCISSORS")
else:
    print ("you have entered the wrong number")


#computer turn
random=random.randint(0,2)


if random==0:
    print(rock+"Computer choice is : ROCKS")
elif random==1:
    print(paper+"Computer choice is : PAPER")
elif random==2:
    print(scissors+"Computer choice is : SCISSORS")


#internal functions
#rocks
if choice=="0"and random==0:
    print("DRAW")
elif choice=="0" and random==2:
    print("YOU WON!!")

#paper
elif choice=="1" and random==1:
    print("DRAW")
elif choice=="1" and random==0:
    print("YOU WON!!")


elif choice=="2" and random==2:
    print("DRAW")
elif choice=="2" and random==1:
    print("YOU WON!!")
else :
    print("YOU LOOSE")