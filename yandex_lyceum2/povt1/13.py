# Далеки издалека
from sys import stdin

lines = stdin.readlines()
print(lines)
ans = 0
for line in lines:
    words = line.lower().split()
    print(words)
    for w in words:
        print(w)
        if w.startswith('далек'):
            ans += 1
            break
print(ans)
