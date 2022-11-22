# create canvas
import dudraw
dudraw.set_canvas_size(500,500)
dudraw.set_x_scale(0,7+1)
dudraw.set_y_scale(0,8+1)

# create connect_four matrix
connect_four = []
for columns in range(7):
    new_column = []
    for rows in range(6):
        new_column.append(0)
    connect_four.append(new_column)

x_radius = 0.4
y_radius = 0.3

def draw_game_board()->None:
    dudraw.set_pen_color(dudraw.DARK_GRAY)
    dudraw.filled_rectangle(4, 3.5, 4, 3.5)
    for i in range(1,8):
        for j in range(1,7):
            if connect_four[i-1][j-1] == 0:
                dudraw.set_pen_color(dudraw.WHITE)
            if connect_four[i-1][j-1] == 1:
                dudraw.set_pen_color(dudraw.RED)
            if connect_four[i-1][j-1] == 2:
                dudraw.set_pen_color(dudraw.YELLOW)
            dudraw.filled_circle(i, j, x_radius)
            dudraw.set_pen_color(dudraw.WHITE)
            dudraw.filled_rectangle(i, 8, x_radius, y_radius)
            dudraw.set_pen_color(dudraw.BLACK)
            dudraw.rectangle(i, 8, x_radius, y_radius)
            dudraw.text(i, 8, "Drop Here")

game_won = False

while game_won == False:
    dudraw.clear(dudraw.LIGHT_GRAY)
    draw_game_board()
    if dudraw.mouse_pressed():
        x = dudraw.mouse_x()
        y = dudraw.mouse_y()

        button_locations = [1,2,3,4,5,6,7]

        for j in range(7):
            if x > button_locations[j] - x_radius and x < button_locations[j] + x_radius:
                if y > 8 - y_radius and y < 8 + y_radius:
                    button_number = j

        if connect_four[button_number][-1] == 0:
            connect_four[button_number][connect_four[button_number].index(0)] = 1
            next_empty_slot = 1
        else:
            dudraw.text(4, 8.5, "This column is full")
            dudraw.show(500)

    # winning conditions
    # for i in range(len(connect_four)):
    #     for j in range(len(connect_four[i])):



        

    dudraw.show(60)
