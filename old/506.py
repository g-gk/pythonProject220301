# Лекарственные травы
n = int(input())
ans = set()
for _ in range(n):
    m = int(input())
    ans |= {input() for _ in range(m)}
print('\n'.join(ans))
