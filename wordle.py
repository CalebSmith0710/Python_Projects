"""
Some bugs need to be fixed

A game of wordle using "usaWords.txt" to populate a list with strings
and using random to select a random index from the list as the target word,
the user has six chances to guess the word before the game is over and the
word is revealed to them. The user can input any five-letter word, each
input counts as a guess unless there are numbers in the word or if the word
is not equal to exaclty five characters.

    Filename: wordle.py
    Author: Caleb Smith
    Date: 1/18/2023
    Internet Source: http://gwicks.net/justwords.html
    Associated Documents: usaWords.txt

"""

from random import randint, random

# Introduction
print("Welcome to Wordle! You have six chances to guess the five-letter word.\nA letter G means you got that letter correct and in the right position.\nA letter Y means you matched that letter, but it is in the wrong position.\nA letter B means that letter does not appear in the correct word.")

# Create word bank
with open("usaWords.txt", "r") as a_file:
    word_bank = []
    word_matrix = [line.strip().replace('\'', '').split() for line in a_file]
    for word_index in range(len(word_matrix)):
        if len(word_matrix[word_index][0]) == 5:
            # word bank is a list of strings
            word_bank.append(word_matrix[word_index][0])

# pick a random word from the list new_line (list of lists)
num = randint(0, len(word_bank))
target_word = word_bank[num]

# TARGET WORD HERE
print(target_word)
# TARGET WORD HERE

guesses = []

game_over = False
guess_count = 0

# loop that continues until the user guesses the word or
# meets the maximum number of guesses
while game_over == False:

    # take guess from user up to five times
    guess = input("What is your guess? ").lower()
    while len(guess) != 5 or guess.isalpha() == False:
        guess = input("Invalid geuss -- input a five-letter word : ").lower()

    # guess count increases each round until it hits 5 (6 guesses total)
    if guess_count == 5:
        game_over = True
    guess_count += 1

    # the game is automatically over if the right word is guessed
    if guess == target_word:
        game_over = True

    # lists of each letter in the target word and the user-inputted guess
    target_word_copy = [letter for letter in target_word]
    guess_copy = [letter for letter in guess]

    # three loops for each color
    for loop_index in range(2):
        if guess == target_word:
            game_over = True

        # nested list to compare each letter of the target to each letter of the guess
        for target_index in range(len(target_word)):
            for guess_index in range(len(guess)):
                if guess == target_word:
                    game_over = True

                # check for greens in the first loop
                if loop_index == 0:
                    if target_word[target_index] == guess[guess_index] and guess_index == target_index:
                        target_word_copy[target_index] = "!"
                        guess_copy[guess_index] = "!"

                # check for yellows in the second loop
                if loop_index == 1:
                    if target_word_copy[target_index] == guess_copy[guess_index] and guess_index != target_index and target_word_copy[target_index] != "G":
                        target_word_copy[target_index] = "?"
                        guess_copy[guess_index] = "?"

    # display letters to player
    for i in range(len(guess_copy)):
        if guess_copy[i] == "!":
            print("G", end = " ")
        if guess_copy[i] == "?":
            print("Y", end = " ")
        else:
            print("B", end = " ")
    print()
    guesses.append(guess)
    for i in range(len(guesses)):
        print(f"Guess {i+1} : {guesses[i]}")

if guess != target_word:
    print(f"You lose, the word was {target_word}.")
if guess_count == 1 and guess == target_word:
    print(f"You win! The word was {target_word}, you got it in {guess_count} guess.")
if guess_count > 1 and guess == target_word:
    print(f"You win! The word was {target_word}, you got it in {guess_count} guesses.")
