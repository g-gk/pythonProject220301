# Далеки издалека
from sys import stdin

lines = stdin.readlines()
ans = 0
for line in lines:
    words = line.lower().split()
    for w in words:
        if w.startswith('далек'):
            ans += 1
            break
print(ans)
