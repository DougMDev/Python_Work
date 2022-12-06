print("Welcome to the tip calculator")
bill = input("What was your total bill? $")
perc = input("What percentage tip would you like to give? 10, 12 or 15? ")
tip = (float(bill) / 100) * int(perc)
split = input("How many people to split the bill? ")

total = round((float(bill) + tip) / int(split), 2)
print(f"Each person should pay: ${total}")

