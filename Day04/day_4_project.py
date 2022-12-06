import random
import project_module

options = [project_module.rock, project_module.paper, project_module.scissors]

player_selection = input("Press 0 for Rock, 1 for Paper and 2 for Scissors ")
formed_ps = int(player_selection)
print(options[formed_ps])


opponent_selection = random.randint(0, 2)
print(options[opponent_selection])

if formed_ps == 0:
    if opponent_selection == 0:
        print("Draw!")
    elif opponent_selection == 1:
        print("Paper Beats Rock! You Lose!")
    else:
        print("Rock Beats Scissors! You Win!........")

if formed_ps == 1:
    if opponent_selection == 0:
        print("Paper Beats Rock! You Win!")
    elif opponent_selection == 1:
        print("Draw!")
    else:
        print("Scissors Beats Paper! You Lose!")

if formed_ps == 2:
    if opponent_selection == 0:
        print("Rock Beats Scissors! You Lose!")
    elif opponent_selection == 1:
        print("Scissors Beats Paper! You Win!")
    else:
        print("Draw!")
