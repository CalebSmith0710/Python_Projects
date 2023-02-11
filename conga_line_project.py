import dudraw
import random
from random import randint

dudraw.set_canvas_size(500, 500)
dudraw.set_x_scale(0, 50)
dudraw.set_y_scale(0, 50)

class Dancer:
    count = 0
    def __init__(self, xp: float = 0, yp: float = 0, tx: float = 0, ty: float = 0, s: float = random.uniform(0.5, 1)):
        self.x_pos = xp
        self.y_pos = yp
        self.target_x = tx
        self.target_y = ty
        self.size = s

    def draw(self):
        dudraw.filled_circle(self.x_pos, self.y_pos, self.size)
        if self.count == len(dancers):
            self.count = 0
        else:
            self.count += 1

    def __str__(self)->str:
        return f"X position: {self.x_pos}, X position type: {type(self.x_pos)}"

    def move(self, other):
        if dancer_index == 0:
            self.x_pos += (self.x_pos - dudraw.mouse_x())
            self.y_pos += (self.y_pos - dudraw.mouse_y())
        else:
            self.x_pos += (self.x_pos - other.x_pos)
            self.y_pos += (self.y_pos - other.y_pos)
        
# main code block
# TODO: Change to range 20 when done
dancers = []
for dancer_index in range(4):
    if dancer_index == 0:
        dancers.append(Dancer(xp = dudraw.mouse_x(), yp = dudraw.mouse_y()))
    else:
        dancers.append(Dancer(xp = randint(1, 49), yp = randint(1, 49)))

    print(dancers[dancer_index])

key = ''
while key != 'q':
    dudraw.clear(dudraw.LIGHT_GRAY)
    for dancer_index in range(len(dancers)):
        dancers[dancer_index].move(dancers[dancer_index - 1])
        dancers[dancer_index].draw()
    dudraw.show(60)