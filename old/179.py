import numpy as np


def make_field(size):
    solution = np.zeros((size, size), dtype='int8')
    for row in range(len(solution)):
        for col in range(row % 2, len(solution[row]), 2):
            solution[row][col] = 1
    return solution


print(make_field(5))
