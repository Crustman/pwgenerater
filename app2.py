#RolerCoaster revised

print("Welcome to the rollercaster!")
height = int(input("What is your height in cm? "))

bill = 0
# bill_child = 0
# bill_youth = 0
# bill_adult = 0
ride_bill = 0
photo = 3
a = 55

if height >= 120:
  print("You can ride the rollercoast!")
  age = int(input("What is your age? "))
  
  # if age >= 45 and age <= 55:
  #   print("Discount")
  if age < 12:
    bill = 5
    ride_bill = 5
    print("\nChild tickets are $5.00")
  elif age >= 45 and age <= 55:
    print("Discount")  
  elif age <= 18:
    bill = 7 
    ride_bill = 7
    print("\nYouth tickets are $7.00")
  else:
    if age >= 18:
      bill = 12
    ride_bill = 12        
    print("\nAdult tickets are $12.00")

  
    
  w_photo = input("\nDo you want a photo taken? Y or N. ")
     
  if w_photo == "y":
    bill += 3
    print(f"The ride comes to ${ride_bill}.00 with the photo, \nadding ${photo}.00 comes to ${bill}.00")
  else: 
    print(f"Your total is ${ride_bill}.00")

else:
  print("Sorry, you are to short.")