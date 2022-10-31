# Лепесток от телескопа, или спаниель в апельсинах
from sys import stdin

words = stdin.readlines()
ans = []
for w in words[1:]:
    t = list(words[0])
    ok = True
    for c in w:
        if c in t:
            t.remove(c)
        else:
            ok = False
            break
    if ok:
        ans.append(w.strip())
print(len(ans))
print('\n'.join(ans))
