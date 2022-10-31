with open('27-b.txt') as f:
    data = f.readlines()
n = int(data[0])
t = list(map(int, data[1:]))
print(n)
cnt = 0
for i in range(n - 102):
    for j in range(i + 102, n):
        if sum(t[i:j]) % 999 == 0:
            cnt += 1
print(cnt)  # 315
