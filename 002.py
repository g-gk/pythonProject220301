s1 = input()
s2 = input()
ans = 0
for c in s2:
    if c in s1:
        ans += 1
print(ans)
