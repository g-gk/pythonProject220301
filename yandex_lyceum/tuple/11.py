# Финал и не финал
n = int(input())
a = [(input(), int(input())) for _ in range(n)]
a.sort(key=lambda x: -x[1])
if n % 2:
    print('\n'.join(sorted(x[0] for x in a[:n // 2 + 1])))
    print('\n'.join(sorted(x[0] for x in a[n // 2 + 1:])))
else:
    print('\n'.join(sorted(x[0] for x in a[:n // 2])))
    print('\n'.join(sorted(x[0] for x in a[n // 2:])))
