# Левый и правый двоичный поиск
from bisect import *

n, k = map(int, input().split())
a = list(map(int, input().split()))
q = list(map(int, input().split()))
ans = ''
for el in q:
    bl, br = bisect_left(a, el), bisect_right(a, el)
    if br - bl > 0:
        ans += str(bl + 1) + ' ' + str(br) + '\n'
    else:
        ans += '0\n'
print(ans[:-1])
