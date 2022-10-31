import sys

t = [elem.strip(' .,/:;!?') for elem in sys.stdin.read().split()]
word = set()
lol = []
words = sorted(filter(lambda x: x[1].istitle(), enumerate(t)), key=lambda el: el[1])
for i in words:
    if i[1] not in word:
        word.add(i[1])
        lol.append(i)

for x in sorted(lol, key=lambda el: el[1]):
    print(f'{x[0]} - {x[1]}')
