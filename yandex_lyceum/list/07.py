# Периодическая десятичная дробь
n = int(input())
ans = []
d = 1
sd = []
while d not in sd:
    sd += [d]
    d *= 10
    d1 = d // n
    ans += [str(d1)]
    d %= n
print(''.join(ans[sd.index(d):]))
