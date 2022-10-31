import numpy as np


def snake(rows, cols):
    lst = np.arange(1, rows * cols + 1).reshape(rows, cols)
    for i in range(len(lst)):
        if i % 2 != 0:
            lst[i] = lst[i][::-1]
    return lst


print(snake(5, 7))
