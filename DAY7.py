# Step 2

import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

end_of_game = False
display_str = ""
lives = 6
display = []
for _ in range(len(chosen_word)):
    display += "_"
while not end_of_game:  # while end_of_game == False
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("Yaaa, You win ! ")
    print(hangman_art.stages[lives])
