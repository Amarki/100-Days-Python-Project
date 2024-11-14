# Day 2 - Tip Calculator
#Purpose: Calculating the total amount of tip each user should pay.

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
percent_tip = tip/100
total_tip_amt = bill * percent_tip
total_bill_with_tip = bill + total_tip_amt
bill_per_person = round(total_bill_with_tip / people,2)
print(f"Each person should pay: ${bill_per_person}")
