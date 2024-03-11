import random
from hangman_art import *
from hangman_words import word_list

chosen_word = random.choice(word_list) ##Choose random word from word list given above.
display = []
word_length = len(chosen_word)
lives = 7
end_of_game = False

print(logo)

for n in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Enter your guessed letter: ").lower()

    # Check guess letter
    if guess in display:
        print(f"You have already enterd {guess}!")
        print(display)
        continue

    for n in range(word_length): ##Loop through each letter of chosen_word to match the enterd letter with current letter.
        if chosen_word[n] == guess:
            display[n] = guess

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life!")
        lives -= 1
        # print(stages[lives])
    if lives == 0:
        end_of_game = True
        print("".join(display))
        print("You lose!")
        print(f"The word was {chosen_word}")
        print(stages[lives])

    elif "_" not in display:
        end_of_game = True
        print("".join(display))
        print("You win!")
        break
    else:
        print(display)

        if lives < 7:
            print(stages[lives])