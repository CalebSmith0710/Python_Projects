"""
A program that asks the user to take candies out of 6 different boxes.
The program correctly detects when an inputted box number is inavlid,
whether it exceeds the number of boxes either positively or negatively
or if the box chosen is empty. The program also switches turns between
users and displays a game over message addressing the player who won.

File Name: candy_game.py
Author: Caleb Smith
Collaborators: None
Internet Sources: w3schools, stackoverflow
"""


#assign variables
number_valid = False
game_won = False
box_not_valid = True
candies_per_box = [0,1,2,3,4,5,6,7]
candies = []
for i in range(6):
    candies.append(candies_per_box)
number_of_candies = 0
box_number = 0
turn = 1

#game introduction/player assignment
print("You are about to play a game called \"Last Candy.\"\nThe objective of the game is to be the player to take the last candy.\nOnce you begin, you will see a row of 6 boxes, each with 7 pieces of candy.\nYou can take as many pieces of candy from any of the boxes as you wish, but be warned,\nif you take too many, the other player may have a chance to win the game.\n")

player_1 = input("Now that we understand the rules, who will be playing the game? (Enter Name) : ")
player_2 = input("Player 2 (Enter Name) : ")

print()

#function that displays the current state of the game
def display_game(candies: list[int])->None:
    # a function that displays the current status of the game
    for i in range(1,7):
        print(f"Box {i}\t\t", end = '')

    print()
    for i in range(1,7):
        try:
            print(f"{candies[i-1][-1]}\t\t", end = '')
        except:
            print("0\t\t", end = '')


    print()

display_game(candies)

#while loop that plays until game_won == True
while game_won == False:
    #turn indicates player turn each round
    if turn == 1:
        player = player_1
    if turn == -1:
        player = player_2

    #player selects box number
    box_number = int(input(f"{player}, which box would you like to choose from? "))

    #while loop to determine if player chose a correct box
    while box_not_valid is True:

        #box number is within the range of boxes
        if box_number <= 6 and box_number >= 1:

            #no more candy in box
            if candies[box_number - 1][-1] == 0:
                box_number = int(input(f"{player}, invalid response, please pick a box that has candy in it : "))

            #there is candy left in the box
            else:
                box_not_valid = False

        #box number not within the range of boxes
        if box_number > 6 or box_number < 1:
            box_number = int(input(f"{player}, invalid response, please pick a number between 1 and 6 : "))
                
    response = input(f"{player}, you are choosing box {box_number}, correct? ")

    if response == "yes" or response == "Yes":

        number_of_candies = int(input(f"Very well, and how many pieces of candy will you take from box {box_number}? "))

        print(f"{player} has taken {number_of_candies} pieces of candy from box {box_number}, leaving {len(candies[box_number - 1]) - (number_of_candies + 1)} pieces of candy left.")

        #updating the value of candies at the given index
        candies[box_number - 1] = candies[box_number - 1][:0 - number_of_candies]

        display_game(candies)

        #winning conditions - if the last index of each box is equal to zero, i.e., no candy left
        if candies[0][-1] == 0 and candies[1][-1] == 0 and candies[2][-1] == 0 and candies[3][-1] == 0 and candies[4][-1] == 0 and candies[5][-1] == 0:
            #exit the while loop, this comes before the variable updates so that
            #the player turn isn't switched, congratulating the loser for winning
            game_won = True

        #variables re-initialize before next turn
        turn = -turn
        box_number = 0
        number_of_candies = 0
        box_number_is_greater_than_zero = True

print(f"{player} wins!!!")