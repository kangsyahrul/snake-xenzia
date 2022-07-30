import enum
import random

import numpy as np

from model.point import Point


class Direction:
    up = Point(0, -1)
    down = Point(0, +1)
    left = Point(-1, 0)
    right = Point(+1, 0)

    DIRECTIONS = {
        'up': up,
        'down': down,
        'left': left,
        'right': right,
    }

    def __init__(self, direction):
        self.point = self.DIRECTIONS[direction]

    def __eq__(self, other):
        return self.point.x == other.point.x and self.point.y == other.point.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __neg__(self):
        if self.point == self.up:
            return Direction('down')
        if self.point == self.down:
            return Direction('up')
        if self.point == self.left:
            return Direction('right')
        if self.point == self.right:
            return Direction('left')


class Snake:

    def __init__(self, board_size):
        self.board_w, self.board_h = board_size
        self.direction = Direction('up')
        self.value = []
        self.length = 0
        self.apple = None

        self.restart()

    def get_head(self):
        return self.value[0]

    def get_body(self):
        return self.value[1:]

    def new_apple(self):
        world = np.zeros((self.board_h, self.board_w), dtype=bool)
        for point in self.value:
            world[point.y][point.x] = True

        empty_fields = []
        for x in range(world.shape[1]):
            for y in range(world.shape[0]):
                if not world[y][x]:
                    empty_fields.append(Point(x, y))

        if len(empty_fields) > 0:
            return random.choice(empty_fields)
        return None

    def restart(self):
        self.direction = Direction('right')
        self.value = [
            Point(self.board_w // 2 + 1, self.board_h // 2),
            Point(self.board_w // 2 + 0, self.board_h // 2),
            Point(self.board_w // 2 - 1, self.board_h // 2),
        ]
        self.apple = self.new_apple()

    def move(self, direction=None):
        if direction is not None:
            if direction == -self.direction:
                return
        else:
            direction = self.direction

        head = self.get_head()
        point_new = head + direction.point
        self.direction = direction
        self.value.insert(0, point_new)
        if head == self.apple:
            new_apple = self.new_apple()
            if new_apple is None:
                return None
            self.apple = new_apple

        else:
            self.value.pop(-1)

        return self.is_outside_world() or self.collision()

    def is_outside_world(self):
        for point in self.value:
            if (point.x < 0 or self.board_w <= point.x) or (point.y < 0 or self.board_h <= point.y):
                return True
        return False

    def collision(self):
        head = self.get_head()
        body = self.get_body()
        for point in body:
            if head == point:
                return True
        return False
