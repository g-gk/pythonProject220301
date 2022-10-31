dnums = {}
data = input()
nums = map(int, data.split(','))
for n in nums:
    if n < 0:
        k = -int(str(-n)[::-1])
        v = False
    else:
        k = int(str(n)[::-1])
        v = k >= 89
    dnums[k] = v
print(dnums)
