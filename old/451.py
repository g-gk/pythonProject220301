from collections import deque

n = int(input())
d1 = deque()
d2 = deque()
for _ in range(n):
    com = input()
    if '+' in com:
        d2.append(com.split()[-1])
    elif '*' in com:
        while len(d1) < len(d2):
            d1.append(d2.popleft())
        d2.appendleft(com.split()[-1])
    elif com == '-':
        while len(d1) < len(d2):
            d1.append(d2.popleft())
        print(d1.popleft())
