import numpy as np


def snake(rows, cols):
    snake = np.arange(1, rows * cols + 1).reshape(rows, cols)
    snake[1::2, ::] = np.flip(snake[1::2, ::])[::-1]
    return snake


print(snake(10, 10))
