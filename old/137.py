import numpy as np


def make_field(n):
    chess = np.zeros((n, n), dtype=np.int8)
    chess[::2, ::2] = 1
    chess[1::2, 1::2] = 1
    return chess


print(make_field(10))
