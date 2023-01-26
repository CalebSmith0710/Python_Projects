import dudraw
from random import randint, random

dudraw.set_canvas_size(400,400)
dudraw.set_x_scale(0, 50)
dudraw.set_y_scale(0, 50)
dudraw.clear(dudraw.BOOK_LIGHT_BLUE)

# create 2D matrix
matrix = [["EMPTY" for col in range(50)] for row in range(50)]

# animation loop
key = ''
while key != 'q':
    if dudraw.mouse_is_pressed():
        x = int(dudraw.mouse_x())
        y = int(dudraw.mouse_y())
        if x >= 47:
            matrix[-y - randint(-3,3)][x - randint(-3 + (52 - x), 3)] = "SAND"
        if x <= 3:
            matrix[-y - randint(-3,3)][x - randint(-3, 0)] = "SAND"
        elif x > 3 and x < 47: 
            matrix[-y - randint(-3, 3)][x - randint(-3, 3)] = "SAND"

    for row_index in range(len(matrix)):
        for col_index in range(len(matrix[row_index])):

            # VARIABLES
            top_index = matrix[len(matrix) - (row_index + 2)][col_index]
            bottom_index = matrix[len(matrix) - (row_index + 1)][col_index]
            current_index = matrix[col_index][row_index]
            # VARIABLES

            if bottom_index == "EMPTY" and top_index == "SAND" and len(matrix) - row_index != 1:
                matrix[len(matrix) - (row_index + 2)][col_index] = "EMPTY"
                matrix[len(matrix) - (row_index + 1)][col_index] = "SAND"
            
            if bottom_index == "SAND" and top_index == "SAND":
            # write a function to tell if theres empty space underneath stacked sand???                   

                # screen edges (prevents index error)
                if col_index == 0:
                    matrix[len(matrix) - (row_index + 1)][col_index + 1] = "SAND"
                    top_index = "EMPTY"

                if col_index == len(matrix[row_index]) - 1:
                    matrix[len(matrix) - (row_index + 1)][col_index - 1] = "SAND"
                    top_index = "EMPTY"

                else:
                
                    # random selection
                    if matrix[len(matrix) - (row_index + 1)][col_index - 1] == "EMPTY" and matrix[len(matrix) - (row_index + 1)][col_index + 1] == "EMPTY":
                        top_index = "EMPTY"
                        direction = randint(1,2)
                        if direction == 1:
                            matrix[len(matrix) - (row_index + 1)][col_index - 1] = "SAND"
                        else:
                            top_index = "SAND"
                            matrix[len(matrix) - (row_index + 1)][col_index + 1] = "SAND"

                    # if one of the sides already has sand
                    else:
                        if matrix[len(matrix) - (row_index + 1)][col_index - 1] == "EMPTY":
                            top_index = "EMPTY"
                            matrix[len(matrix) - (row_index + 1)][col_index - 1] = "SAND"
                    
                        if matrix[len(matrix) - (row_index + 1)][col_index + 1] == "EMPTY":
                            top_index = "EMPTY"
                            matrix[len(matrix) - (row_index + 1)][col_index + 1] = "SAND"
                    

            if current_index == "EMPTY":
                dudraw.set_pen_color(dudraw.BOOK_LIGHT_BLUE)
                dudraw.filled_square(row_index + 0.5, len(matrix) - col_index-0.5, 0.5)

            if current_index == "SAND":
                dudraw.set_pen_color(dudraw.YELLOW)
                dudraw.filled_square(row_index + 0.5, len(matrix) - col_index-0.5, 0.5)

    if dudraw.has_next_key_typed():
        key = dudraw.next_key_typed
    
    dudraw.show(40)

