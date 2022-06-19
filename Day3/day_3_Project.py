# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

q1 = input("You come to a crossroads, You can head 'right' or 'left', which way do you choose? ").lower()
if q1 == "left":
    q2 = input("You approach a large river. you could 'wait' for a boat or attempt to cross by 'swimming'. ").lower()
    if q2 == "wait":
        q3 = input("You approach a castle with 3 doors, one 'red', one 'yellow' and one 'blue' which do you choose to enter? ").lower()
        if q3 == "yellow":
            print("Congratulations! You find the gold and live happily ever after!!")
        elif q3 == "red":
            print("You enter a dark room, suddenly flames surround you. so hot! you burn to death in an instant.")
        elif q3 == "blue":
            print("you hear a roar, so quick! the Beast strikes you down in one swipe.")
        else:
            print("Your indecision drover you to madness. You fall into a deep slumber, never to awaken.")
    else:
        print("You are attacked by an angry trout, you try to pull your self to safety but drown..")
else: 
    print("you Trip over a rock, breaking your shin, you pass out and die due to exposure.")


