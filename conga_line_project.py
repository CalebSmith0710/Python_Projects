import dudraw
import random
from random import randint

dudraw.set_canvas_size(500, 500)
dudraw.set_x_scale(0, 50)
dudraw.set_y_scale(0, 50)

class Dancer:
    count = 0
    def __init__(self, xp: float = 1, yp: float = 1, tx: float = 1, ty: float = 1, s: float = random.uniform(1, 1.5)):
        self.x_pos = xp
        self.y_pos = yp
        self.target_x = tx
        self.target_y = ty
        self.size = s

    def draw(self):
        dudraw.filled_circle(dancers[dancer_index].x_pos, dancers[dancer_index].y_pos, dancers[dancer_index].size)

    def move(self):
        if dancer_index == 0:
            dancers[dancer_index].x_pos -= (dancers[dancer_index].x_pos - dudraw.mouse_x()) * 0.05
            dancers[dancer_index].y_pos -= (dancers[dancer_index].y_pos - dudraw.mouse_y()) * 0.05
        else:
            dancers[dancer_index].x_pos -= (dancers[dancer_index].x_pos - dancers[dancer_index - 1].x_pos) * 0.05
            dancers[dancer_index].y_pos -= (dancers[dancer_index].y_pos - dancers[dancer_index - 1].y_pos) * 0.05

    def set_target(self):
        if dancer_index > 0:
            dancers[dancer_index].target_x = dancers[dancer_index - 1].x_pos
            dancers[dancer_index].target_y = dancers[dancer_index - 1].y_pos
        else:
            dancers[dancer_index].target_x = dudraw.mouse_x()
            dancers[dancer_index].target_y = dudraw.mouse_y()

# main code block
dancers = [Dancer() for dancer_index in range(10)]
for dancer_index in range(len(dancers)):
    if dancer_index > 0:
        dancers[dancer_index].x_pos = random.uniform(1, 49)
        dancers[dancer_index].y_pos = random.uniform(1, 49)
        dancers[dancer_index].size = random.uniform(1, 1.5)
    else:
        dancers[dancer_index].x_pos = dudraw.mouse_x()
        dancers[dancer_index].y_pos = dudraw.mouse_y()
        dancers[dancer_index].size = random.uniform(1, 1.5)

key = ''
while key != 'q':
    dudraw.clear(dudraw.LIGHT_GRAY)

    for dancer_index in range(len(dancers)):
        dancers[dancer_index].move()
        dancers[dancer_index].set_target()
        dancers[dancer_index].draw()

    dudraw.show(60)
    