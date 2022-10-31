# НОК
# Напишите программу, которая вычисляет наименьшее общее кратное двух чисел.
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


a, b = map(int, input().split())
print(a * b // gcd(a, b))
