# Ближайшее число
# Напишите программу, которая находит в массиве элемент, самый близкий по
# величине к данному числу.
a = list(map(int, input().split()))
n = int(input())
ans = a[0]
for i in range(1, len(a)):
    if abs(a[i] - n) < abs(ans - n):
        ans = a[i]
print(ans)
