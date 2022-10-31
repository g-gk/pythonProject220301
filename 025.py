numbers = map(int, input().split())
numbers_new = [x for x in numbers if x % 2]
print(*numbers_new)
