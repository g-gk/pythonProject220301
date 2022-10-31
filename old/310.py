# Выдача сдачи
# Имеется неограниченное количество монет в 1, 2, 5, 10 рублей.
# Определите, сколькими способами можно выдать сдачу в n рублей.
# Например, 5 рублей можно выдать четырьмя способами: 5=2+2+1=2+1+1+1=1+1+1+1+1.
n = int(input())
count = 0
for n1 in range(n + 1):
    for n2 in range((n - n1) // 2 + 1):
        for n5 in range((n - n1 - n2) // 5 + 1):
            for n10 in range((n - n1 - n2 - n5) // 10 + 1):
                if 10 * n10 + 5 * n5 + 2 * n2 + n1 == n:
                    count += 1
print(count)
