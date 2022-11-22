# create canvas
import dudraw
dudraw.set_canvas_size(500,500)
dudraw.set_x_scale(0,7)
dudraw.set_y_scale(0,8)

# create connect_four matrix
connect_four = []
for rows in range(6):
    new_row = []
    for columns in range(7):
        new_row.append(0)
    connect_four.append(new_row)

def draw_game_board()->None:
    dudraw.set_pen_color(dudraw.DARK_GRAY)
    dudraw.filled_rectangle(3.5, 3, 3.5, 3)
    for i in range(1,6):
        for j in range(1,7):
            if connect_four[i-1][j-1] == 0:
                dudraw.set_pen_color(dudraw.WHITE)
            if connect_four[i-1][j-1] == 1:
                dudraw.set_pen_color(dudraw.RED)
            if connect_four[i-1][j-1] == 2:
                dudraw.set_pen_color(dudraw.YELLOW)
            dudraw.filled_circle(j, i, 0.4)
            dudraw.filled_rectangle(j, 7, 0.4, 0.3)
            dudraw.set_pen_color(dudraw.BLACK)
            dudraw.rectangle(j, 7, 0.4, 0.3)
            dudraw.text(j, 7, "Drop Here")

game_won = False

while game_won == False:
    dudraw.clear(dudraw.LIGHT_GRAY)
    draw_game_board()
    if dudraw.mouse_pressed():
        if dudraw.mouse_x >
    dudraw.show(60)
