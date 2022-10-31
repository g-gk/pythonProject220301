a = [170, 166, 176, 166, 176, 168, 179, 163, 168, 161]
a.sort()
print(*a)  # 161 163 166 166 168 168 170 176 176 179
print(1, a[-1] - a[0])  # 18
print(2, max(a[-1] - a[-5], a[-5] - a[-10]))  # 11
mx = 0
for i in range(len(a) - 1):
    mx = max(mx, a[i + 1] - a[i])
print(3, mx)  # 6
mn = 1000000
for i in range(len(a) - 3):
    mx = min(mx, a[i + 3] - a[i])
print(4, mx)  # 2
