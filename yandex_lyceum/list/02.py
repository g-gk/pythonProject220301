# Не бином Ньютона
n = int(input())
a = [int(input()) for _ in range(n)]
b = [a[i] + a[i + 1] for i in range(n - 1)]
print(*b, sep='\n')
