# Больше своих соседей
# Дан список чисел. Определите, сколько в этом списке элементов, которые больше
# двух своих соседей, и выведите количество таких элементов.
a = list(map(int, input().split()))
ans = 0
for i in range(1, len(a) - 1):
    if a[i - 1] < a[i] > a[i + 1]:
        ans += 1
print(ans)