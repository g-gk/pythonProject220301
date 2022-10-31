# Дислексия
ru = input().lower().split()
words = input().lower().split()
ans = []
d = {}
for w in ru:
    sw = ''.join(sorted(w))
    d[sw] = d.get(sw, set()) | {w}
for word in words:
    sw = ''.join(sorted(word))
    if sw in d:
        if len(d[sw]) == 1 and word in d[sw]:
            ans.append(word)
        else:
            ans.append('#' * len(word))
    else:
        ans.append(word)
print(' '.join(ans))
