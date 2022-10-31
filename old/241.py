n = 1
for _ in range(15):
    n += n % 10
print(1, n)  # 68
n = 1
cnt = 0
for _ in range(1000000):
    n += n % 10
    cnt += 1
    if n == 2022:
        break
print(2, cnt)  # 405
n = 1
cnt = 0
mx = 0
mx7 = 0
for _ in range(10000000):
    n += n % 10
    if len(str(n)) == 3:
        cnt += 1
        mx = max(mx, n)
    elif len(str(n)) == 7:
        mx7 = max(mx7, n)
    if bin(n).count('1') == 1:
        print(n)
print(3, cnt)  # 180
print(4, mx)  # 996
print(5, mx7)  # 9999996
