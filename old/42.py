import itertools

sok_dict = input().lower().split()
text = input().lower().split()
result = list()
for i in text:
    t = list(map(lambda x: ''.join(x) in sok_dict and ''.join(x) != i, itertools.permutations(i)))
    if any(t):
        result.append(len(i) * '#')
    else:
        result.append(i)
print(' '.join(result))
