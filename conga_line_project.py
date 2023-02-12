"""
A program using dudraw and classes to create a list
of circle objects that trail eachother, with the first
in the list trailing the current mouse position. Pressing
'n' will spawn a new 'dancer' and pressing 'q' will close
the pygame window.

    Filename: conga_line_project.py
    Authors: Caleb Smith
    Date: 2/11/2023
    Collaborators: None
    Internet Source: None
"""

import dudraw
import random
from random import randint

dudraw.set_canvas_size(500, 500)
dudraw.set_x_scale(0, 50)
dudraw.set_y_scale(0, 50)

class Dancer: # instantiate Dancer object with instance variables for current position, target position and size
    def __init__(self, xp: float = 1, yp: float = 1, tx: float = 1, ty: float = 1, s: float = random.uniform(0.5, 1)):
        self.x_pos = xp
        self.y_pos = yp
        self.target_x = tx
        self.target_y = ty
        self.size = s

    def draw(self): # draw function
        dudraw.filled_circle(dancers[dancer_index].x_pos, dancers[dancer_index].y_pos, dancers[dancer_index].size)

    def move(self): # move function
        if dancer_index == 0: # the first Dancer instance will pursue the current mouse position at a speed of 5 % of the distance between itself and the mouse position
            dancers[dancer_index].x_pos -= (dancers[dancer_index].x_pos - dudraw.mouse_x()) * 0.05
            dancers[dancer_index].y_pos -= (dancers[dancer_index].y_pos - dudraw.mouse_y()) * 0.05

        else: # following Dancer instances will pursue the Dancer instance at the previous index in the list of dancers at a speed of 5 %  of the distance between itself and the Dancer it is pursuing
            dancers[dancer_index].x_pos -= (dancers[dancer_index].x_pos - dancers[dancer_index - 1].x_pos) * 0.05
            dancers[dancer_index].y_pos -= (dancers[dancer_index].y_pos - dancers[dancer_index - 1].y_pos) * 0.05

    def set_target(self): # set_target function to acquire the target for the Dancer instance to pursue
        if dancer_index > 0: # the 'backup' Dancer objects will acquire the previous dancer's position in list of dancers as their target
            dancers[dancer_index].target_x = dancers[dancer_index - 1].x_pos
            dancers[dancer_index].target_y = dancers[dancer_index - 1].y_pos
        else: # the 'lead' Dancer object will acquire the current mouse position as it's target
            dancers[dancer_index].target_x = dudraw.mouse_x()
            dancers[dancer_index].target_y = dudraw.mouse_y()

# main code block
dancers = [Dancer() for dancer_index in range(5)] # dancers is initialized to have 5 Dancer objects

for dancer_index in range(len(dancers)): # assign variables to each Dancer object (didn't work by putting this in the list comprehension for some reason)

    if dancer_index > 0: # the 'backup' Dancers are initialized to a random x and y and a random size between 0.5 and 1
        dancers[dancer_index].x_pos = random.uniform(1, 49)
        dancers[dancer_index].y_pos = random.uniform(1, 49)
        dancers[dancer_index].size = random.uniform(0.5, 1)
    else: # the 'lead' Dancer is initialized to the current mouse position and a random size between 0.5 and 1
        dancers[dancer_index].x_pos = dudraw.mouse_x()
        dancers[dancer_index].y_pos = dudraw.mouse_y()
        dancers[dancer_index].size = random.uniform(0.5, 1)

# animation loop
key = ''
while key != 'q':
    dudraw.clear(dudraw.LIGHT_GRAY)

    for dancer_index in range(len(dancers)): # loop through Dancer objects and call move, set_target and draw functions
        dancers[dancer_index].move()
        dancers[dancer_index].set_target()
        dancers[dancer_index].draw()

    if dudraw.has_next_key_typed(): # check if a key was pressed
        key = dudraw.next_key_typed() # store the key in a variable 'key'
        if key == 'n': # pressing 'n' instantiates a new Dancer object and appends it to dancers
            dancers.append(Dancer(xp = random.uniform(1, 49), yp = random.uniform(1, 49), s = random.uniform(0.5, 1)))
            key = '' # reset the key as to not spawn new Dancer instances with every step of the animation

    dudraw.show(60)
    