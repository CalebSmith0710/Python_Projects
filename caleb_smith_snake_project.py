"""
A game of snake using a doubly linked list. The values of the list correspond
with the x and y position of each segment of the snake. If the x and y position
of the head of the snake intersects with itself or is off the game board, the
program ends and "Game over" is printed to the terminal. If the snake head 
intersects with a food pellet, an element is appended to the list - represented
by the snake growing in size - and a new food pellet is spawned somewhere else
on the game board randomly.

*Requires doubly_linked_list.py to be in the same working directory*

File Name: caleb_smith_snake_project.py
Author: Caleb Smith
Date: 4/10/2022
Course: COMP 1353
Assignment: Project 1
Collaborators: None
Internet Sources: None
"""


# import doubly linked list class
from doubly_linked_list import DoublyLinkedList
import dudraw
import random
import sys
from sys import exit

difficulties = [12, 8, 5, 2]
difficulty = int(input("What difficulty would you like?\n12 - Easy\n8 - Normal\n5 - Hard\n2 - Extra Hard\n"))
while difficulty not in difficulties:
    difficulty = int(input("Invalid input, choose from the following difficulties:\n12 - Easy\n8 - Normal\n5 - Hard\n2 - Extra Hard\n"))

dudraw.set_canvas_size(500,500)
dudraw.set_x_scale(-1, 21)
dudraw.set_y_scale(-1, 21)

game_over_variable = 0 # 1 means game over

class SnakeBody:
    def __init__(self):
        self.snake_list = DoublyLinkedList() # initialize empty snake list
        self.direction = '' # Directions: (a - left, w - up, d - right, s - down)
        for snake_segment in range(8, 12): # populate snake on game board
            self.snake_list.add_last([snake_segment, 9])
        self.head_snake = self.snake_list.header.next # head of snake
        self.tail_snake = self.snake_list.trailer.prev # tail of snake
        self.food_x = random.randint(1, 19) # x position of food pellet
        self.food_y = random.randint(1, 19) # y position of food pellet

    def draw(self): # walk the list and draw a square based on the values of each element in the list
        dudraw.clear(dudraw.WHITE)
        dudraw.set_pen_color(dudraw.BLACK)
        temp_node = self.snake_list.header
        while temp_node.next is not self.snake_list.trailer or None:
            temp_node = temp_node.next
            dudraw.filled_square(temp_node.value[0], temp_node.value[1], 0.5)

    def __Str__(self)->str: # print contents of the list
        return f"{self.snake_list}"

    def move(self, key): # move the snake each frame, takes 'key' from main code block

        self.direction = key

        if self.direction == 'a': # moves the snake to the left
            self.tail_snake.value[0] = self.head_snake.value[0] - 1
            self.tail_snake.value[1] = self.head_snake.value[1]

        if self.direction == 'd': # moves the snake to the right
            self.tail_snake.value[0] = self.head_snake.value[0] + 1
            self.tail_snake.value[1] = self.head_snake.value[1]

        if self.direction == 'w': # moves the snake up
            self.tail_snake.value[1] = self.head_snake.value[1] + 1
            self.tail_snake.value[0] = self.head_snake.value[0]

        if self.direction == 's': # moves the snake down
            self.tail_snake.value[1] = self.head_snake.value[1] - 1
            self.tail_snake.value[0] = self.head_snake.value[0]

        # game ends if the snake goes out of bounds
        if self.head_snake.value[0] > 21 or self.head_snake.value[1] > 21 or self.head_snake.value[0] < 0 or self.head_snake.value[1] < 0:
            print("Game over")
            sys.exit()

    def change_list(self): # every frame, the tail moves to the head position and 'head' and 'tail' change
        self.snake_list.trailer.prev = self.tail_snake.prev
        self.snake_list.header.next = self.tail_snake
        self.tail_snake.prev.next = self.snake_list.trailer
        self.tail_snake.next = self.head_snake
        self.tail_snake.prev = self.snake_list.header
        self.head_snake.prev = self.tail_snake

        self.tail_snake = self.snake_list.trailer.prev # updated tail reference
        self.head_snake = self.snake_list.header.next # updated head reference

    def grow(self): # adds a snake segment inbetween the third and second to last elements to avoid problems with tail changing
        self.snake_list.add_between([self.tail_snake.value[0] - 1, self.tail_snake.value[1] - 1], snake.tail_snake.prev.prev, snake.tail_snake.prev)

    def collision(self): # determines if the head x and y values coincide with any of the x and y values in the body
        temp_node = self.head_snake.next
        while temp_node.next is not None:
            if temp_node.value[1] == self.head_snake.value[1] and temp_node.value[0] == self.head_snake.value[0]: # game ends if body is equal to head
                print("Game over")
                sys.exit()
            temp_node = temp_node.next

    def randomize_pellet_location(self): # used to randomize the location of the pellet when the last one is eaten
        self.food_x = random.randint(1, 19)
        self.food_y = random.randint(1, 19)

    def draw_food_pellet(self): # draws the food pellet
        dudraw.set_pen_color(dudraw.YELLOW)
        dudraw.filled_square(self.food_x, self.food_y, 0.5)

    def eat(self)->bool: # returns true if the pellet was eaten and false if it was not
        if self.head_snake.value[0] == self.food_x and self.head_snake.value[1] == self.food_y:
            return True
        return False

snake = SnakeBody()

limit = 20 #number of frames to allow to pass before snake moves
timer = 0  #a timer to keep track of number of frames that passed
key = ''
while key != "q":
    timer += 1

    if dudraw.has_next_key_typed():
        key = dudraw.next_key_typed()            

    if timer == limit:
        timer = 0
        
        snake.draw() # draw the snake
        snake.change_list() # change head and tail position as well as references
        snake.draw_food_pellet() # draws the food pellet each frame
        if key == "w" or key == "a" or key == "s" or key == "d":
            snake.move(key) # pressing any of the four keys causes the snake to move in the associated direction
        snake.collision() # checks for collision each frame
        if snake.eat() == True: # conditions for when the food pellet is eaten
            snake.grow() # snake grows by 1 when he eats
            snake.randomize_pellet_location() # a new pellet location is determined

    dudraw.show(difficulty) # the number entered for difficulty by the player determines how fast the snake moves

print("Game over") # if the user presses q, the game ends