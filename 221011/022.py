r = int(input())
sr = bin(r)[2:]
n = len(sr)
sr = '0' * (12 - n) + sr
# print(sr)
si = ''
for i in range(0, n - 2, 3):
    a = sr[i:i + 3]
    if a in ('001', '010', '100', '111'):
        print(-1)
        exit(0)
    si += a[:2]
# print(si)
print(int(si, 2))
