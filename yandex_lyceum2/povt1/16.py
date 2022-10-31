# Вопросительное повествование без восклицаний
from sys import stdin

data = stdin.readlines()
ans = {}
for d in data:
    t = d.rstrip()
    if t and t[-1].isdigit():
        n = int(t.split()[-1])
        k = ' '.join(t.split()[:-1])
        if n in ans and k not in ans[n]:
            ans[n].append(k)
        elif n not in ans:
            ans[n] = [k]
for k in sorted(ans.keys()):
    print(f'{k}:', ', '.join(ans[k]))
