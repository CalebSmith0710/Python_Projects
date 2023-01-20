import random
import argparse
from termcolor import colored

parser = argparse.ArgumentParser(description = "Wordle: A Word Game")

parser.add_argument(
    '--word-len',
    nargs = 1,
    type = int,
    choices = [i for i in range(9) if i >=3],
    default = 5
    help = 'The length of the target word to use.')

args = parser.parse_args()

word_len = args.word_len

with open('usaWords.txt', 'r') as f:
    lines = [line.strip().upper() for line in f]

word_bank = [word for word in lines if len(word) == word_len and word.isalpha() == True]

target_word = random.choice(word_bank)

intro_text = (
    f"Welcome to Wordle! You have six chances to guess the {word_len}-letter word.\n"
    f"\t A letter surrounded by {colored(' green ', on_color = 'on_green')} means you got that letter correct and in the right position.\n"
    f"\t A letter surrounded by {colored(' yellow ', on_color = 'on_yellow')} means you matched that letter, but it is in the wrong position.\n"
    f"\t A letter surrounded by {colored(' red ', on_color = 'on_red')} means that letter does not appear in the correct word.\n"
)

print(intro_text)

# Global stateful variables
guess_hist = []

clue_matrix = []

guess_count = 1

game_won = False

while game_won == False and guess_count <= 6:
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

    """
    Requirements:
      1. if a letter in the guess appears twice and one of them is in the right spot, 
         the other should be highlighted red if that letter doesn't appear again in the target.
         If it does appear again in the target, highlight it yellow.
      2. if the guess contains the same letter twice, and both are in the wrong spot,
         and the target word only has that letter once, then only highlight the first instance of that letter yellow.
      
      Example 1:
        target_word = 'TREPA'
        guess = 'STEEP'
        output colors = [R Y G R Y]

      Example 2:
        target_word = 'MAKER'
        guess = 'PEELE'
        output = [R Y R R R]
    """
    mapped = [(g, t) for g,t in zip(list(guess), list(target_word))]

    evaluated = []
    # matched = set([j for j, k in mapped if j == k])

    for i, (j, k) in enumerate(mapped):
        if j == k:
            current_clues.append(colored("{:^3}".format(guess[i]), on_color = 'on_green'))
        if 
        evaluated.append(mapped.pop(i))

    for i in range(5):
        if guess[i] == target_word[i]:
            current_clues.append(colored("{:^3}".format(guess[i]), on_color = 'on_green'))
        elif guess[i] in target_word:
            if 
            current_clues.append(colored("{:^3}".format(guess[i]), on_color = 'on_yellow'))
        else:
            current_clues.append(colored("{:^3}".format(guess[i]), on_color = 'on_red'))

    clue_matrix.append(current_clues)

    # prints the clue matrix consisting of color-coded cells
    print('\n\n'.join([' '.join([item for item in row]) for row in clue_matrix]), end = '\n\n')

    if guess == target_word:
        game_won = True

if game_won == True:
    print(
        f"You win! The target word was {target_word} and you got it in {guess_count}",
        "guess." if guess_count == 1 else "guesses.", sep = " ")
else:
    print(f"You lose, the word was {target_word}.")