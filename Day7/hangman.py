#Step 1 
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
rand_word = random.choice(word_list)
word_len = len(rand_word)

lives = 6
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

    if guess not in rand_word:
        lives -= 1
        print(stages[lives])
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