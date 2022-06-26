#Step 1 
import random
import hangman_displays
import hangman_wordlist

rand_word = random.choice(hangman_wordlist.word_list)
word_len = len(rand_word)

lives = 6
#Testing code
print(f'Pssst, the solution is {rand_word}.')

display = []
for _ in range(word_len):
    display += "_"

end_of_game = False

print(hangman_displays.logo)

while not end_of_game:
    guess = input("Guess a Letter!: ").lower()

    #Check guessed letter
    for position in range(word_len):
        letter = rand_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in rand_word:
        lives -= 1
        print(hangman_displays.stages[lives])
        print(f"No Match!! You have {lives} lives left")
        if lives == 0:
            end_of_game = True
            print("Game Over!!, You Lose!")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("YOU WIN!!!")
        print(f"The Letter was {rand_word}")
    
    if lives == 0:
        print("You Lose :(")