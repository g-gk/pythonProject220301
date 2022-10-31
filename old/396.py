from bisect import *

n, k = map(int, input().split())
a = list(map(int, input().split()))
q = list(map(int, input().split()))
ans = []
for el in q:
    if bisect_right(a, el) - bisect_left(a, el) > 0:
        ans += ['YES']
    else:
        ans += ['NO']
print('\n'.join(ans))
