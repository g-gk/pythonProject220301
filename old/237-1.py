n, a, b = [int(input()) for _ in range(3)]
c = 0
for i in range(n):
    if (i + 1) % a == 0 or (i + 1) % b == 0:
        c += 1
print(c)
