import sys
import re

data_1 = []
data_2 = []
prov = []
data = sys.stdin.read()
data = re.sub(r'[^\w\s]', '', data)
data = [pair for pair in enumerate(data.split())]
for i in data:
    if i[1][0] == i[1][0].capitalize():
        if i[1] not in prov:
            data_1.append(i)
            prov.append(i[1])
prov.sort()
for i in prov:
    for j in data_1:
        if i == j[1]:
            data_2.append(j)
            continue
for i in data_2:
    print(f'{i[0]} - {i[1]}')
