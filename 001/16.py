# Обозначим частное от деления целочисленного натурального числа a на
# натуральное число b как a div b, а остаток как a mod b. Например, 13 div 3 = 4,
# 13 mod 3 = 1.
# Алгоритм вычисления значения функции F(a, b), где a и b – целые
# неотрицательные числа, задан следующими соотношениями:
# F(0, b) = b;
# F(a, b) = F(a div 10, 10b + (a mod 10)), если a > 0.
# Укажите наименьшее значение a, для которого F(a, 0) = 1248163264.

def f(a, b):
    if a == 0:
        return b
    elif a > 0:
        return f(a // 10, 10 * b + a % 10)


for a in range(1, 1_000_000):
    print(a, f(a, 0))
    if f(a, 0) == 1248163264:
        print(a)
        break
print('1248163264'[::-1])  # 4623618421
