#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

# rand_int = random.randint(0, 2)
# rand_word = word_list[rand_int]
rand_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {rand_word}.')

#TO DO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

guess = input("Guess a Letter! ").lower()

#TO DO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

for letter in rand_word:
    if letter == guess:
        print("Correct")
    else:
        print("Wrong")
