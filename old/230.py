n = int(input())
a = [int(input()) for _ in range(n)]
b = []
x = a.pop()
while len(b) < x:
    b.append(x)
    x = a.pop()
print(len(b) - 1)
