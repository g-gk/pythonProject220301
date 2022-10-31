# Гвоздики
n = int(input())
a = [-100000] + list(map(int, input().split())) + [100000]
# print(a)
s = []
# a.sort()
i = 1
while i < n + 1:
    if a[i] - a[i - 1] < a[i + 1] - a[i]:
        s.append(a[i] - a[i - 1])
    else:
        s.append(a[i + 1] - a[i])
        i += 1
    i += 1
print(sum(s))
