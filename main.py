
# main.py

import random
from hangman_words import word_list
from hangman_art import logo, stages

# Display the hangman logo at the start of the game
print(logo)

# Randomly choose a word from the word list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Create a list to keep track of guessed letters
display = ["_"] * word_length

# Initialize game state variables
end_of_game = False
lives = 6

# Game loop
while not end_of_game:
    # Ask the user to guess a letter
    guess = input("Guess a letter: ").lower()

    # Check if the user has already guessed this letter
    if guess in display:
        print(f"You've already guessed {guess}")
    else:
        # Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        # If the guessed letter is not in the chosen word
        if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")
                print(f"The word was: {chosen_word}")

    # Join all the elements in the list and turn it into a string
    print(" ".join(display))

    # Check if the user has got all the letters
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Display the current stage of the hangman
    print(stages[lives])
