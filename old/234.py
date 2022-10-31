with open('subbotnik.txt') as f:
    a = f.readlines()
a = sorted(list(map(int, a)))
print(a)
print(max(a) - min(a))
n = len(a)
mn = 1000
for i in range(n - 9):
    mn = min(mn, a[i + 9] - a[i])
print(mn)
for i in range(n - 9):
    if mn == a[i + 9] - a[i]:
        print(*a[i:i + 10])
