# Количество различных элементов
# Дан список, упорядоченный по неубыванию элементов в нём.
# Определите, сколько в нём различных элементов.
a = list(map(int, input().split()))
print(len(set(a)))
