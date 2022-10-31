with open('27-a.txt') as f:
    data = f.readlines()
n = int(data[0])  # 919
t = list(map(int, data[1:]))
# print(n)
cnt = 0
for i in range(n - 100):
    for j in range(i + 101, n + 1):
        if sum(t[i:j]) % 999 == 0:
            cnt += 1
print(cnt)  # 317
