# Только миллиардеры
print('\n'.join(','.join(y for y in x.split(',') if int(y) >= 10 ** 9) for x in input().split(';')))
