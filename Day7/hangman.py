#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]
rand_word = random.choice(word_list)
word_len = len(rand_word)

#Testing code
print(f'Pssst, the solution is {rand_word}.')

display = []
for _ in range(word_len):
    display += "_"

end_of_game = False

while not end_of_game:
    guess = input("Guess a Letter!: ").lower()

    #Check guessed letter
    for position in range(word_len):
        letter = rand_word[position]
        if letter == guess:
            display[position] = letter

    print(display)

    if "_" not in display:
        end_of_game = True
        print("YOU WIN!!!")