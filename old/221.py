import numpy as np


def super_sort(rows, cols):
    a = np.random.randint(1, 100, (rows, cols), dtype=np.int8)
    b = a.copy()
    b[::, ::2] = np.sort(b[::, ::2], axis=0)
    b[::, 1::2] = np.flip(np.sort(b[::, 1::2], axis=0))[::, ::-1]
    return (a, b)


print(*super_sort(3, 5), sep='\n')
