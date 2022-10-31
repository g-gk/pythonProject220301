# Кинотеатр
# В кинотеатре n рядов по m мест в каждом. В двумерном массиве хранится информация о
# проданных билетах, число 1 означает, что билет на данное место уже продан, число 0
# означает, что место свободно. Поступил запрос на продажу k билетов на соседние места в
# одном ряду. Определите, можно ли выполнить такой запрос.
n, m = map(int, input().split())
a = [input().replace(' ', '') for _ in range(n)]
k = int(input())
for i in range(n):
    if '0' * k in a[i]:
        print(i + 1)
        exit(0)
print(0)