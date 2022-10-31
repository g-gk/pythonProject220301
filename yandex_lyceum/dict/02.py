# Характеристики двоичных чисел
nums = list(map(int, input().split()))
dnums = []
for num in nums:
    n2 = bin(num)[2:]
    dnums.append({'digits': len(n2), 'units': n2.count('1'), 'zeros': n2.count('0')})
print(dnums)
