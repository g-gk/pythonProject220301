# Прикладная нумерология
def sd(n):
    res = 0
    while n > 0:
        res += n % 10
        n //= 10
    return res


hours = set(map(int, input().split()))
minuts = set(map(int, input().split()))
for mm in range(24 * 60):
    h, m = mm // 60, mm % 60
    if h in hours and m in minuts and sd(h) != sd(m):
        print(f'{h:02d}:{m:02d}')
