# Переставить min и max
# Дан список чисел. В списке все элементы различны.
# Поменяйте местами минимальный и максимальный элемент этого списка.
a = list(map(int, input().split()))
imax, imin = a.index(max(a)), a.index(min(a))
a[imin], a[imax] = a[imax], a[imin]
print(*a)
