# Объединение последовательностей


def merge(a, b):
    i, j = 0, 0
    res = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            res += [a[i]]
            i += 1
        elif b[j] < a[i]:
            res += [b[j]]
            j += 1
        else:
            res += [a[i]]
            i += 1
            j += 1
    return res + a[i:] + b[j:]


x = int(input())
a = [(i + 1) ** 2 for i in range(x)]
b = [(i + 1) ** 3 for i in range(x)]
c = merge(a, b)
# print(*a)
# print(*b)
# print(*c)
print(c[x - 1])
