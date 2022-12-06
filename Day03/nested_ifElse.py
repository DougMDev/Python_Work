# age = int(input("What is your age? "))
# height = int(input("How tall are you in cm? "))

# if height >= 120:
#     if age >= 18:
#         print("You are tall enough to ride & need to purchase an adult ticket")
#     else:
#         print("You are tall enough to ride & need to purchase a child ticket")
# else:
#     print("You are not tall enough to ride")


height = int(input("How tall are you in cm? "))

if height >= 120:
    age = int(input("What is your age? "))
    if age < 9:
        print("Go Ahead, Tickets are £3")
    elif age < 16:
        print("Go Ahead, Tickets are £4")
    else:
        print("Go Ahead, Tickets are £5")
else:
    print("Sorry, you are not tall enough")