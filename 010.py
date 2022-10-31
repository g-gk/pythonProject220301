t = {-337, -3, -2, -1, 1, 2, 3, 337}
ans = set()
for a in t:
    for b in t - {a}:
        for c in t - {a, b}:
            for d in t - {a, b, c}:
                for e in t - {a, b, c, d}:
                    if a * b * c * d * e == 2022:
                        s = a + b + c + d + e
                        if s not in ans:
                            ans.add(s)
                            print(f'{a} + {b} + {c} + {d} + {e} = {s}', )

# 1 + 2 + 3 + -337 + -1 = -332
# 1 + 2 + 337 + -1 + -3 = 336
# 1 + 3 + 337 + -1 + -2 = 338
# 1 + -337 + -2 + -3 + -1 = -342
