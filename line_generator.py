"""
A program which generates a connected path of lines
and shifts the position of the entire path slightly
with each iteration. Lines do not "bounce" when
they reach the boundary of the canvas.

File Name: line_generator.py
Author: Caleb Smith
Collaborators: None
Internet Sources: None
Associated Documents: None
"""

import dudraw
from random import randint, random

dudraw.set_canvas_size(500,500)
dudraw.set_pen_width(0.005)

#assign empty lists for x and y positions as well as x and y velocities
x = []
y = []
x_velocity = []
y_velocity = []


#populate lists x, y, x_velocity and y_velocity
for i in range(10):
    x.append(random())
    y.append(random())
    x_velocity.append((random() * 0.03))
    y_velocity.append((random() * 0.03))

#animation for loop
for i in range(100):
    #random pen color for every iteration of the loop
    dudraw.set_pen_color_rgb(randint(0,255), randint(0,255), randint(0,255))
    #assign variables to be a random integers from
    #the lists x_velocity and y_velocity
    #this determines how much the lines will shift
    #this happens every 10 steps, not including the first
    for j in range(10):
        dudraw.line(x[j], y[j], x[j-1], y[j-1])
        x[j] += x_velocity[j]
        y[j] += y_velocity[j]
        if x[j] > 1 or x[j] < 0:
            x_velocity[j] = -x_velocity[j]
        if y[j] > 1 or y[j] < 0:
            y_velocity[j] = -y_velocity[j]


    dudraw.show(60)



