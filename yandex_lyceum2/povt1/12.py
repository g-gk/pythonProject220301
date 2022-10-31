# Далеки
from sys import stdin

lines = stdin.readlines()
ans = 0
for line in lines:
    if 'далек' in line.lower():
        ans += 1
print(ans)
