n = 1
c = 0
mx = 0
for i in range(10000000):
    n += n % 10
    # if n == 2022:
    # print(i + 1)
    if len(str(n)) == 3:
        c += 1
    if len(str(n)) == 7 and n > mx:
        mx = n
    if bin(n).count('1') == 1:
        print(n)
# print(n)
# print(c)
# print(mx)
