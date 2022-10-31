# Средние в статистике
a = sorted(map(float, input().split()))
n = len(a)
if n % 2:
    print(sum(a) / n, a[n // 2])
else:
    print(sum(a) / n, (a[n // 2 - 1] + a[n // 2]) / 2)
