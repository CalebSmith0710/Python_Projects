import dudraw
from random import randint, random
dudraw.set_canvas_size(500,500)
dudraw.set_x_scale(0, 100)
dudraw.set_y_scale(0, 100)

class Dancer:
    def __init__(self, dp: list = [], tp: list = [], s: int = randint(1, 3)):
        self.dancer_position = dp
        self.target_position = tp
        self.size = s

    def draw():
        pass

    def move():
        pass

# main code block
dancers = []
for dancer_index in range(4):

    if dancer_index == 0:
        dancers.append(Dancer(dp = [dudraw.mouse_x, dudraw.mouse_y], tp = [dudraw.mouse_x, dudraw.mouse_y]))
    if dancer_index > 1:
        dancers.append(Dancer(dp = [randint(0, 100), randint(0, 100)], tp = [dancers[dancer_index - 1][0], dancers[dancer_index - 1][1]]))
    else:
        dancers.append(Dancer(dp = [randint(0, 100), randint(0, 100)], tp = [dancers[0][0], dancers[0][1]]))

# animation loop
key = ''
while key != 'q':

    if dudraw.has_next_key_typed:
        key = dudraw.next_key_typed

    dudraw.clear(dudraw.LIGHT_GRAY)
    for dancer_index in range(len(dancers)):
        dancers[dancer_index].draw()
        dancers[dancer_index].move()
    dudraw.show(60)
