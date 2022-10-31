# Два Пути
s = int(input())
b = [[int(input()) for _ in range(s)]]
b += [b[0].copy()]
n = int(input())
for _ in range(n):
    k = [int(input()) for _ in range(3)]
    b[k[0] - 1][k[1]] += k[2]
print(*b[0])
print(*b[1])
print(sum(b[0][i] == b[1][i] for i in range(s)))
