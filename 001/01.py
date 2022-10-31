count = 0
for i in range(100, 1000):
    sum_digits = sum(int(c) for c in str(i))
    if sum_digits == 14:
        print(i, end=' ')
        count += 1
print()
print(count)
