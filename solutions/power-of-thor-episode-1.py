import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]


def debug(msg):
    print(msg, file=sys.stderr)


class Thor:
    def __init__(self, init_x, init_y, light_x, light_y):
        self.x = init_x
        self.y = init_y
        self.lx = light_x
        self.ly = light_y

    def move(self, direction):
        if 'N' in direction:
            self.y -= 1
        if 'S' in direction:
            self.y += 1
        if 'E' in direction:
            self.x += 1
        if 'W' in direction:
            self.x -= 1

        print(direction)

    def move_towards_light(self):
        def above_light():
            return self.y < self.ly

        def below_light():
            return self.y > self.ly

        def east_of_light():
            return self.x > self.lx

        def west_of_light():
            return self.x < self.lx

        direction = ''
        if above_light():
            direction += 'S'
        if below_light():
            direction += 'N'
        if west_of_light():
            direction += 'E'
        if east_of_light():
            direction += 'W'

        self.move(direction)


thor = Thor(initial_tx, initial_ty, light_x, light_y)

# game loop
while True:
    # The remaining amount of turns Thor can move. Do not remove this line.
    remaining_turns = int(input())

    thor.move_towards_light()
