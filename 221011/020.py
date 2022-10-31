a, c, m, x_prev, n = map(int, input().split())
sum_ = 0
for _ in range(n):
    x = (a * x_prev + c) % m
    sum_ += x
    x_prev = x
print(f'{sum_ / n:.4f}')
