# Вася строит дом
a, b, d = map(int, input().split())
if a > b:
    a, b = b, a
ab = b - a
if ab % 2 == 0:
    ans = a + ab // 2
    s = min(ans % d, d - ans % d)
    print(ans, s)
else:
    ans1 = a + ab // 2
    s1 = min(ans1 % d, d - ans1 % d)
    ans2 = ans1 + 1
    s2 = min(ans2 % d, d - ans2 % d)
    if s1 < s2:
        print(ans1, s1)
    else:
        print(ans2, s2)
