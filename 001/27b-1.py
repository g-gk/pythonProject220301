with open('27-b.txt') as f:
    data = f.readlines()
n = int(data[0])
t = list(map(int, data[1:]))
# print(n)
cnt, s = 0, 0
line = [0]
for i in range(99):
    s += t[i]
    line.append(s)
k = [0] * 999
for i in range(99, n):
    s += t[i]
    cnt += k[s % 999]
    ost = line[(i + 1) % 100] % 999
    k[ost] += 1
    line[(i + 1) % 100] = s
print(cnt)  # 1801612662
