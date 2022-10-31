# Сортировка слиянием


def merge(a, b):
    i, j = 0, 0
    res = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            res += [a[i]]
            i += 1
        else:
            res += [b[j]]
            j += 1
    return res + a[i:] + b[j:]


def msort(a):
    n = len(a)
    if n == 1:
        return a
    m = n // 2
    a1, a2 = a[:m], a[m:]
    return merge(msort(a1), msort(a2))


n = int(input())
a = list(map(int, input().split()))
print(*msort(a))
