
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("\nWelcome to the PyPassword generator!\n")
no_letters=int(input(f"How much letter do you want in your password?\n"))
no_numbers=int(input(f"How much numbers do you want in your password?\n"))
no_symbols=int(input(f"How much symbols do you want in your password?\n"))

#shuffled password generator

password=[]

for character in range(0,no_letters):
    password.append(random.choice(letters))

for character in range(0, no_numbers):
    password.append(random.choice(numbers))

for character in range(0, no_symbols):
    password.append(random.choice(symbols))

print(password)
random.shuffle(password)
print(password)

Password=""
for character in password:
    Password+=character

print(f"\nyour password is: {Password}")