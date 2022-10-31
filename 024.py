x = input()
cnt, mx, mn = 0, 149, 191
while x != '!':
    y = int(x)
    if 150 <= y <= 190:
        cnt += 1
        mn = min(mn, y)
        mx = max(mx, y)
    x = input()
print(cnt)
print(mn, mx)
