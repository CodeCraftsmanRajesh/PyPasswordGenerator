import random

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
          'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbol = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

print("Welcome to Password Generator")

no_of_letters = int(input("How many letters would you like in your password?\n"))
no_of_symbols = int(input("How many symbols would you like?\n"))
no_of_digits = int(input("How many numbers would you like?\n"))


"""
 <--- EASY VERSION
 password = ""
# adding letters in passwords
for i in range(no_of_letters):
    password += random.choice(letter)

# adding symbols in passwords
for i in range(no_of_symbols):
    password += random.choice(symbol)

# adding digits in passwords
for i in range(no_of_digits):
    password += random.choice(numbers)

print(f"Your generated password is: {password}")
"""

# HARD VERSION OF PASSWORD GENERATOR
password_list = []

# adding letter in password
for i in range(no_of_letters):
    password_list.append(random.choice(letter))

# adding symbols in password
for i in range(no_of_symbols):
    password_list.append(random.choice(symbol))

# adding numbers in password
for i in range(no_of_digits):
    password_list.append(random.choice(numbers))

# print(password_list)
random.shuffle(password_list)
password = ""

for char in password_list:
    password += char


print("Your generated password is: "+ password)
