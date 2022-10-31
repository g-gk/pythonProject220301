# F. Домики
n = int(input())
d = list(map(int, input().split()))
if n == 1:
    print(0)
elif n == 2:
    print(sum(d))
else:
    mn = min(d)
    print((n - 2) * mn + sum(d))
