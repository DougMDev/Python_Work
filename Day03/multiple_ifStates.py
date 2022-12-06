height = int(input("How tall are you in cm? "))

if height >= 120:
    bill = 0
    age = int(input("What is your age? "))
    if age < 9:
        print("Go Ahead, Tickets are £3")
        ticket = 3
    elif age < 16:
        print("Go Ahead, Tickets are £4")
        ticket = 4
    else:
        print("Go Ahead, Tickets are £5")
        ticket = 5
    photo = input("Do you want a Photo? ")
    photoformed = photo.upper()
    if photoformed == "YES":
        bill = 3
    newTotal = ticket + bill
    print(f"Thankyou for riding, your total bill is £{newTotal}")
else:
    print("Sorry, you are not tall enough")