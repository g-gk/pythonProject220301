# Далеки далеко
from sys import stdin

ok = ['далек', 'далеки', 'далека', 'далеков', 'далеку',
      'далекам', 'далеком', 'далеками', 'далеке', 'далеках']
lines = stdin.readlines()
ans = 0
for line in lines:
    words = line.lower().split()
    for w in words:
        if w in ok:
            ans += 1
            break
print(ans)
