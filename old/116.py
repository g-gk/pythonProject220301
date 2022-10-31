import numpy as np


def generation(solution):
    for _ in range(10):
        solution = np.array(list(solution), dtype=np.uint8)
        E = np.roll(solution, 1, 0)
        e = np.roll(solution, 0, 0)
        Ee = np.roll(solution, -1, 0)
        solution = np.ones(len(solution), dtype=np.uint8) & (((E != 0) & (e != 1) & (Ee != 1)) |
                                                             ((E != 1) & (e != 0) & (Ee != 0)) |
                                                             ((E != 1) & (e != 0) & (Ee != 1)) |
                                                             ((E != 1) & (e != 1) & (Ee != 0)))
        solution = np.array(solution, dtype='<U32')
    solution = ''.join(solution)
    return solution


print(generation(
    "1001000101111100000101111001011011101101101111110111110000000000000011000001011001100011111101001001"))
