print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))

people = int(input("How many people will be splitting the bill?"))

tip_percent = tip / 100
total_tip_amount = bill * tip_percent
total_bill = bill + total_tip_amount
split_amount = total_bill / people
result = format(split_amount, ".2f")

print(f"Each person should pay: ${result}")
