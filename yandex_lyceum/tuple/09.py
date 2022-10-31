# A272727
n = int(input())
a = [0]
while len(a) < n:
    cur = 0
    for i in range(len(a)):
        if a[i] == a[-i - 1]:
            cur += 1
    a += [cur]
print('\n'.join(map(str, a)))
