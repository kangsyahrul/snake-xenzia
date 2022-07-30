import cv2
import time

from model.world import World
from model.snake import Snake
from model.snake import Direction

# GAME SETTING
BOARD_SIZE_W, BOARD_SIZE_H = BOARD_SIZE = (16, 16)

# SCREEN SETTING
BLOCK_SIZE_W, BLOCK_SIZE_H = BLOCK_SIZE = (16, 16)
PADDING_X, PADDING_Y = PADDING = (24, 24)
WINDOW_SIZE_W, WINDOW_SIZE_H = WINDOW_SIZE = (PADDING_X * 2 + BOARD_SIZE_W * BLOCK_SIZE_W, PADDING_Y * 2 + BOARD_SIZE_H * BLOCK_SIZE_H)


def main():

    world = World(WINDOW_SIZE, PADDING, BOARD_SIZE, BLOCK_SIZE)
    snake = Snake(BOARD_SIZE)

    duration = 0.25
    time_start = time.time()
    time_click = time.time()
    is_game_over = False
    while not is_game_over:
        img = world.draw_snake(snake)

        cv2.imshow('Snake Xenzia', img)

        key = cv2.waitKey(int(1000 * (duration - (time.time() - time_click))))
        time_click = time.time()
        if key == ord('q'):
            break

        if key == ord('a'):
            is_game_over = snake.move(Direction('left'))

        if key == ord('d'):
            is_game_over = snake.move(Direction('right'))

        if key == ord('w'):
            is_game_over = snake.move(Direction('up'))

        if key == ord('s'):
            is_game_over = snake.move(Direction('down'))

        if key == -1:
            is_game_over = snake.move()

    if is_game_over:
        print('Game Over')


if __name__ == '__main__':
    main()
