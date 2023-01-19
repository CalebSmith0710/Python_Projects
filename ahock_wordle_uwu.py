import random
from termcolor import colored

with open('usaWords.txt', 'r') as f:
    lines = [line.strip().upper() for line in f]

word_bank = [word for word in lines if len(word) == 5 and word.isalpha() == True]

target_word = random.choice(word_bank)

intro_text = (
    "Welcome to Wordle! You have six chances to guess the five-letter word.\n"
    f"\t A letter surrounded by {colored(' green ', on_color = 'on_green')} means you got that letter correct and in the right position.\n"
    f"\t A letter surrounded by {colored(' yellow ', on_color = 'on_yellow')} means you matched that letter, but it is in the wrong position.\n"
    f"\t A letter surrounded by {colored(' red ', on_color = 'on_red')} means that letter does not appear in the correct word.\n"
)

print(intro_text)

# Global stateful variables
guess_hist = []

clue_matrix = []

guess_count = 1

game_over = False

while game_over == False and guess_count <= 6:
    if guess_count == 1:
        guess = input("What is your guess? ").strip().upper()
    else:
        guess = input("Incorrect! What is your next guess? ").strip().upper()

    while guess not in word_bank:
        guess = input("Invalid guess -- please enter a valid five-letter English word: ").strip().upper()

    while guess in guess_hist:
        guess = input("Invalid guess -- you've already chosen this word. Please pick another: ").strip().upper()

    guess_hist.append(guess)

    guess_count += 1

    current_clues = []

    for i in range(5):
        if guess[i] == target_word[i]:
            current_clues.append(colored("{:^3}".format(guess[i]), on_color = 'on_green'))
        elif guess[i] in target_word:
            current_clues.append(colored("{:^3}".format(guess[i]), on_color = 'on_yellow'))
        else:
            current_clues.append(colored("{:^3}".format(guess[i]), on_color = 'on_red'))

    clue_matrix.append(current_clues)

    # prints the clue matrix consisting of color-coded cells
    print('\n\n'.join([' '.join(['{:4}'.format(item) for item in row]) for row in clue_matrix]), end = '\n\n')

    if guess == target_word:
        game_over = True

if guess == target_word:
    print(f"You win! The target word was {target_word} and you got it in {guess_count}", "guess." if guess_count == 1 else "guesses.", sep = " ")
else:
    print(f"You lose, the word was {target_word}.")