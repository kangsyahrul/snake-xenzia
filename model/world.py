import cv2
import numpy as np


class World:

    def __init__(self, window_size, padding, board_size, block_size):
        self.window_w, self.window_h = window_size
        self.padding_w, self.padding_h = padding
        self.board_w, self.board_h = board_size
        self.block_w, self.block_h = block_size

        self.background = self.create_background()
        self.value = self.create_board()
        self.shape = self.value.shape

    def create_board(self):
        return np.zeros((self.board_h, self.board_w), dtype=np.uint8)

    def create_background(self):
        img = np.zeros((self.window_h, self.window_w, 3), dtype=np.uint8)

        x1, y1 = self.padding_w, self.padding_h
        x2, y2 = self.window_w - self.padding_w, self.window_h - self.padding_h

        img = cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 0), -1)

        for x in range(self.padding_w, self.padding_w + self.block_w * (self.board_w + 1), self.block_w):
            y1 = self.padding_h
            y2 = self.padding_h + self.block_h * self.board_h
            img = cv2.line(img, (x, y1), (x, y2), (75, 75, 75), 1, cv2.LINE_AA)

        for y in range(self.padding_h, self.padding_h + self.block_h * (self.board_h + 1), self.block_h):
            x1 = self.padding_w
            x2 = self.padding_w + self.block_w * self.board_w
            img = cv2.line(img, (x1, y), (x2, y), (75, 75, 75), 1, cv2.LINE_AA)

        return img

    def draw_object(self, img, point, color, l=0, t=0, r=0, b=0, scaler=4):
        x1 = self.padding_w + (point.x + 0) * self.block_w
        x2 = self.padding_w + (point.x + 1) * self.block_w

        y1 = self.padding_h + (point.y + 0) * self.block_h
        y2 = self.padding_h + (point.y + 1) * self.block_h

        img = cv2.rectangle(img, (x1 + l * scaler, y1 + t * scaler), (x2 - r * scaler, y2 - b * scaler), color, -1)
        return img

    def draw_snake(self, snake):
        img = self.background.copy()

        # Draw apple
        img = self.draw_object(img, snake.apple, (200, 75, 75))

        # Draw Snake
        for i, point in enumerate(snake.value):
            color = (200, 200, 200)
            if i == 0:
                # Head
                color = (75, 75, 200)

            img = self.draw_object(img, point, color)

        return img
