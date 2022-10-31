import functools
from sys import stdin

words = []
for w in stdin:
    words.append(w.split('\n')[0])


def func(prev_res, next_element):
    return prev_res if (prev_res < next_element) else next_element


print(functools.reduce(func, words, words[0]))
