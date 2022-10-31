# Новые блюда
m = int(input())
set1 = {input() for _ in range(m)}
n = int(input())
set2 = set()
for _ in range(n):
    k = int(input())
    set2 |= {input() for _ in range(k)}
print('\n'.join(set1 - set2))
