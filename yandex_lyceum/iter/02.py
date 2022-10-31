# Выгодная покупка
from sys import stdin

data = stdin.readlines()
mn = min(data[1:], key=lambda x: sum(map(int, x.split('\t')[1:]))).split('\t')
print(mn[0])
for el in zip(data[0].split('\t')[1:], mn[1:]):
    print('\t'.join((el[0].strip(), el[1].strip())))
