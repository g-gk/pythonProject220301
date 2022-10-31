# Репосты
n = int(input())
line1 = input()
words = line1.split()
d = {words[0]: int(words[-1])}
names = [words[0]]
lines = []
for _ in range(n - 1):
    line = input()
    lines.append(line)
    words = line.split()
    names.append(words[0])

for line in reversed(lines):
    words = line.split()
    d[words[0]] = d.get(words[0], 0) + int(words[-1])
    d[words[4][:-1]] = d.get(words[4][:-1], 0) + d[words[0]]

for name in names:
    print(d[name])
