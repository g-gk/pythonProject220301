# Сумма произведений соседних чисел
# По заданной последовательности a1, a2, …, an чисел вычислите сумму a1⋅a2+a2⋅a3+⋯+an−1⋅an.
n = int(input())
a = int(input())
summ = 0
for i in range(n - 1):
    b = int(input())
    summ += a * b
    a = b
print(summ)
