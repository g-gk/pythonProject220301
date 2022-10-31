n, a, b = [int(input()) for _ in range(3)]
nums = set()
for i in range(a, n + 1, a):
    nums.add(i)
for i in range(b, n + 1, b):
    nums.add(i)
print(len(nums))
