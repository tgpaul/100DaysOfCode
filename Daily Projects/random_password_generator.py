# This is a program that should generate a random password for the User
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# List will contain the random selections
password_list = []
for number in range(0, nr_letters):
    selection = random.choice(letters)
    password_list.append(selection)

for number in range(0, nr_symbols):
    selection = random.choice(symbols)
    password_list.append(selection)

for number in range(0, nr_numbers):
    selection = random.choice(numbers)
    password_list.append(selection)

# Shuffle the list (or else the number/symbols/letters would be clumped together)
random.shuffle(password_list)

# Convert the list into a string
password = ""
for index in range(0, len(password_list)):
    password += password_list[index]

print(f"The random password is:\n{password}")