print("Welcome to Pizza Junction")
size = input("What size pizza do you want, s, m, l ? ")
add_pep = input("Do you want pepperoni y or n? ")
cheese = input("Would you like extra cheese y or n? ")

bill = 0;

if size == "s":
  bill += 15
elif size == "m":
  bill += 20
else:
  bill += 25

if add_pep == "y":
  if size == "s":
    bill += 2
else:
  bill += 3

if cheese == "y":
  bill += 1

print(f"Your final bill is: ${bill}")