#Step 1 
from pickle import FALSE
import random
word_list = ["aardvark", "baboon", "camel"]

# rand_int = random.randint(0, 2)
# rand_word = word_list[rand_int]
rand_word = random.choice(word_list)
word_len = len(rand_word)

#Testing code
print(f'Pssst, the solution is {rand_word}.')

display = []
for letter in rand_word:
    display.append("_")
print(display)

end_of_game = False

while not end_of_game:
    guess = input("Guess a Letter! ").lower()

    #Check guessed letter
    for position in range(word_len):
        letter = rand_word[position]
        if letter == guess:
            display[position] = letter

    print(display)

if "_" not in display:
    end_of_game = True
    print("You WIN!!!")