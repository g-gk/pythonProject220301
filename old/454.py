# Симметрическая разность множеств
n = int(input())
a = set(map(int, input().split()))
m = int(input())
a ^= set(map(int, input().split()))
print(len(a))
print(*sorted(a))
