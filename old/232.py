mn = 10000
mx = -1
for i in range(1, 1000):
    a = i
    p = a // 2 + a % 2
    a -= p
    v = a // 2 + a % 2
    a -= v
    t = a // 2 + a % 2
    a -= t
    if a == 15:
        mn = min(mn, i)
        mx = max(mx, i)
print(mn, mx)
# 1 8 15
# 7 56 63
# 15 120 127
