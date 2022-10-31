# Белый список
n = int(input())
wl = [input() for _ in range(n)]
ans = []
m = int(input())
for _ in range(m):
    x = input()
    if x in wl:
        ans += [x]
print('\n'.join(ans))
