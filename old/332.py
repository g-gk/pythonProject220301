# Медиана
# В списке нечётное число элементов, при этом все элементы различны. Найдите медиану
# списка: элемент, который стоял бы ровно посередине списка, если список отсортировать.
# При решении этой задачи нельзя модифицировать данный список
# (в том числе и сортировать его), использовать вспомогательные списки.
# Программа должна вывести единственное число — значение медианного элемента в списке.
n = int(input())
a = list(map(int, input().split()))
for x in a:
    cnt = 0
    for y in a:
        if y < x:
            cnt += 1
    if cnt == n // 2:
        print(x)
        break
