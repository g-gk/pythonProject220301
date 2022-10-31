# Юбилейные монеты
from sys import stdin

data = stdin.readlines()
s = set()
ans = 0
for x in data:
    a = x.split()
    name = ''.join(x).strip()
    if name in s:
        ans += int(a[0])
    else:
        s.add(name)
print(ans)
