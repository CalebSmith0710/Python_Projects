"""
A program which generates an image based on Richard Gregory's
"slanted lines" optical illusion using dudraw.

File Name: optical_illusion.py
Author: Caleb Smith
Collaborators: None
Internet Sources: None
Associated Documents: None
"""

import dudraw

#8x8 checkerboard pattern
radius = (1 / 8) / 2
height = (1 / 10) / 2
x_pos = radius * 2
y_pos = height
line_x1 = 0
line_y1 = 0
line_x2 = 1
line_y2 = 0

#columns
for i in range(1, 12):
    if i % 2 == 0:
        x_pos = radius / 3
    else:
        x_pos = radius / 3 - radius 
    #rows
    for j in range(1, 12):
        if i % 2 != 0:
            if j % 2 == 0:
                dudraw.set_pen_color_rgb(255,177,234)
                dudraw.filled_rectangle(x_pos, y_pos, radius, height)
                x_pos += radius * 2
            else:
                dudraw.set_pen_color_rgb(132,22,139)
                dudraw.filled_rectangle(x_pos, y_pos, radius, height)
                x_pos += radius * 2
        else:
            if j % 2 == 0:
                dudraw.set_pen_color_rgb(132,22,139)
                dudraw.filled_rectangle(x_pos, y_pos, radius, height)
                x_pos += radius * 2
            else:
                dudraw.set_pen_color_rgb(255,177,234)
                dudraw.filled_rectangle(x_pos, y_pos, radius, height)
                x_pos += radius * 2
    y_pos += 2 * height
    dudraw.set_pen_color(dudraw.LIGHT_GRAY)
    dudraw.set_pen_width(height / 15)
    dudraw.line(line_x1, line_y1, line_x2, line_y2)
    line_y1 += height * 2
    line_y2 += height * 2
    
dudraw.show(float('inf'))