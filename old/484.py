# Джек-Победитель-Великанов
from sys import stdin

n = int(stdin.readline())
words = stdin.read().split('*')[:-1]
ans = []
for i in range(n):
    ans += ['-'.join(words.pop().split())]
print(', '.join(ans))
