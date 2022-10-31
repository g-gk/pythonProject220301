# Обратное число
from sys import stdin


def f(a, n, p):
    if n == 0:
        return 1
    elif n % 2:
        return f(a, n - 1, p) * a % p
    return f(a, n // 2, p) ** 2 % p


data = list(map(str.strip, stdin))
# print(data)
# t = int(input())
t = int(data[0])
ans = ''
for i in range(t):
    # p, a = map(int, input().split())
    p, a = map(int, data[i + 1].split())
    ans += str(f(a, p - 2, p)) + '\n'
print(ans[:-1])
