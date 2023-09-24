# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Initialize variables to store generated characters
password_letters = ""
password_symbols = ""
password_numbers = ""

# Generate characters
for i in range(0, nr_letters):
  random_number = random.randint(0, len(letters) - 1)
  password_letters += letters[random_number]


for i in range(0, nr_symbols):
  random_number = random.randint(0, len(symbols) - 1)
  password_symbols += symbols[random_number]

for i in range(0, nr_numbers):
  random_number = random.randint(0, len(numbers) - 1)
  password_numbers += numbers[random_number]

# Combine and shuffle the characters to create the password
password_total = password_letters + password_symbols + password_numbers
password_total= list(password_total)
random.shuffle(password_total)
password_total = ''.join(password_total)
print(f"Your Password is {password_total}")