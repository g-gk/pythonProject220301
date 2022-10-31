# Похожие массивы
# Назовём два массива похожими, если они состоят из одних и тех же элементов
# (без учёта кратности). По двум данным массивам выясните, похожие они или нет.
n1 = int(input())
a1 = list(map(int, input().split()))
n2 = int(input())
a2 = list(map(int, input().split()))
if set(a1) == set(a2):
    print('YES')
else:
    print('NO')
