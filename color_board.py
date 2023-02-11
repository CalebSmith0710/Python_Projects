"""
Demonstration of 2D lists using lists and dudraw to
manipulate elements of a list and provide a visual
display of manipulations.

File Name: color_board.py
Author: Caleb Smith
Collaborators: None
Internet Sources: None
"""

import dudraw

# function to create 2D list
def draw_grid()->list:
    dudraw.set_canvas_size(500,600)
    dudraw.set_x_scale(0,10)
    dudraw.set_y_scale(0,12)
    dudraw.set_pen_color(dudraw.BLACK)
    dudraw.set_pen_width(0.02)
    

    rows = []
    for i in range(12):
        columns = []
        for j in range(10):
            columns.append(0)
        rows.append(columns)
    return rows

rows = draw_grid()

# animation loop
active = True

while active == True:
    dudraw.clear(dudraw.WHITE)
    for i in range(len(rows)):
        # draw the elements of each row
        for j in range(len(rows[i])):
            # draw a filled rectangle with a starting color of white, slowly
            # becoming more and more red with each click
            dudraw.set_pen_color_rgb(255, 255 - rows[i][j] * 2, 255 - rows[i][j] * 2)
            dudraw.filled_rectangle(j + .5, 12 - i - .5, .5, .5)
            # draw outlines of rectangles
            dudraw.set_pen_color(dudraw.BLACK)
            dudraw.rectangle(j + .5, 12 - i- .5, .5, .5)
            # draw a number in each rectangle representing the number
            # of times it's been clicked
            dudraw.text(j + 0.5, 12 - i - 0.5, f'{rows[i][j]}')
    # if the mouse is clicked, add 1 to the list index associated
    # with the location of the click
    if dudraw.mouse_is_pressed():
        rows[int(-dudraw.mouse_y())-1][int(dudraw.mouse_x())] += 1
    # if the user inputs "q", the program will end
    if dudraw.has_next_key_typed():
        if dudraw.next_key_typed() == "q":
            active = False
    dudraw.show(60)
    


