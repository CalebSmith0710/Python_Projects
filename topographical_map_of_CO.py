"""
A program that reads the file "CO_elevations_feet.txt" and
populates a 2D list. The program then finds the highest 
elevation, which is used to determine RGB values for
a topical map of the state of colorado created using the
2D list "elevation_matrix" and dudraw. Using the list
indeces, the user can click on a given point on the map
and a box will pop up displaying the elevation of the
given point.

File Name: topographical_map_of_CO.py
Author: Caleb Smith
Internet Sources: W3Schools
Associated Documents: CO_elevations_in_feet.txt

"""

import dudraw

# create 2D list
with open("CO_elevations_feet.txt", "r") as a_file:
    elevation_matrix = []
    for line in a_file:
        new_line = []
        new_line = line.split()
        elevation_matrix.append(new_line)

# determine highest elevation
highest_elevation = 0
for row in range(len(elevation_matrix)):
    for elevation in range(len(elevation_matrix[row])):
        elevation_matrix[row][elevation] = int(elevation_matrix[row][elevation])
        if elevation_matrix[row][elevation] > highest_elevation:
            highest_elevation = elevation_matrix[row][elevation]

# create canvas
dudraw.set_canvas_size(500,500)
dudraw.set_x_scale(0,761)
dudraw.set_y_scale(0,561)

# animation loop
while True:
    dudraw.clear(dudraw.LIGHT_GRAY)
    for row in range(1, len(elevation_matrix)):
        for column in range(1, len(elevation_matrix[row])):
            # a variable to calculate RGB value based on elevation and relation
            # to the maximum elevation of the data set
            color_variable = int(((elevation_matrix[row][column] / highest_elevation) * 100) * 2)
            dudraw.set_pen_color_rgb(255 - color_variable, 255 - color_variable, 255 - color_variable)
            dudraw.filled_square(column, 561 - row, 1)
    # when the user clicks on a given point, the x and y location
    # are used to create a variable which accesses the index
    # assocated with the x and y position
    if dudraw.mouse_is_pressed():
        x = int(dudraw.mouse_x())
        y = int(dudraw.mouse_y())
        value = elevation_matrix[y][x]
        dudraw.set_pen_color(dudraw.BLACK)
        dudraw.rectangle(100, 50, 100, 50)
        dudraw.text(100, 50, f"{value}")
    dudraw.show(60)