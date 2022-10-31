# Резиновые слова
w = input()
n = len(w)
m = n // 2
if n % 2:
    print(' ' * m, w[m], sep='')
    for i in range(1, m + 1):
        print(" " * (m - i), w[m - i], " " * (i * 2 - 1), w[m + i], sep='')
else:
    for i in range(m):
        print(" " * (m - i - 1), w[m - i - 1], " " * (i * 2), w[m + i], sep='')
