#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

# Day Goal: Understanding data types and manipulating strings

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
percentage_tip = int(input("What percentage would you like to tip? (10, 12 or 15) "))
nos = int(input("How many people to split the bill? "))

total_tip = bill*(percentage_tip/100)

total_bill = bill + total_tip

per_person = round(total_bill/nos,2)

print(f"Each person should pay: {per_person}")