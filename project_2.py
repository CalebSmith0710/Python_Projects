"""

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
print(target_word)

game_over = False
guess_count = 0
while game_over == False:
    # take guess from user up to five times
    guess = input("What is your guess? ")
    while len(guess) != 5:
        guess = input("Invalid geuss -- input a five-letter word : ")
        
    if guess_count == 5:
        game_over = True
    guess_count += 1

    if guess == target_word:
        game_over = True

    # lists of each letter in the target and guess
    target_word_copy = [letter for letter in target_word]
    guess_copy = [letter for letter in guess]

    # start of code I may have to change
    for target_index in range(len(target_word)):
        for guess_index in range(len(guess)):

            # check to see if the letter is green
            if target_word_copy[target_index] == guess_copy[guess_index] and target_index == guess_index and target_word_copy[target_index] != "G":
                target_word_copy[target_index] = "G"
                guess_copy[guess_index] = "G"
            # check to see if the letter is yellow
            if target_word_copy[target_index] == guess_copy[guess_index] and target_index != guess_index and guess_copy[guess_index] != "G" and guess_copy[guess_index] != "Y" and guess_copy[guess_index] != "B":
                target_word_copy[target_index] = "Y"
                guess_copy[guess_index] = "Y"
            # check to see if the letter is black
            if target_word_copy[target_index] != guess_copy[guess_index] and target_index != guess_index and guess_copy[guess_index] != "G" and guess_copy[guess_index] != "Y" and guess_copy[guess_index] != "B":
                target_word_copy[target_index] = "B"
                guess_copy[guess_index] = "B"

    # display letters to player
    for i in range(len(guess_copy)):
        print(guess_copy[i], end = " ")
    print()



if guess != target_word:
    print(f"You lose, the word was {target_word}.")
if guess_count == 1 and guess == target_word:
    print(f"You win! The word was {target_word}, you got it in {guess_count} guess.")
if guess_count > 1 and guess == target_word:
    print(f"You win! The word was {target_word}, you got it in {guess_count} guesses.")
