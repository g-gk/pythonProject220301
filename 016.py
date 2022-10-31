n = {1, 2, 3, 4, 5}
ans = set()
for a in n:
    for b in n - {a}:
        for c in n - {a, b}:
            for d in n - {a, b, c}:
                x = a * 1000 + b * 100 + c * 10 + d
                if x % 6 == 0:
                    ans.add(x)
print(len(ans))
print(*sorted(ans), sep='\n')
