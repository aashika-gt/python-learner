import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("\nWelcome to the Password generator!\n")
no_letters=int(input(f"How many letter do you want in your password?\n"))
no_numbers=int(input(f"How many numbers do you want in your password?\n"))
no_symbols=int(input(f"How many symbols do you want in your password?\n"))

#sequence password generator (first letters then numbers and last symbols)
password=""

for elements in range(0,no_letters):
    password+=random.choice(letters)

for elements in range(0,no_numbers):
    password+=random.choice(numbers)

for elements in range(0, no_symbols):
    password += random.choice(symbols)

print(f"your password is :{password}")
