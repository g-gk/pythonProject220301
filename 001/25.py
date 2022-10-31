# Пусть M(k) = 7 000 000 + k, где k – натуральное число.
# Найдите пять наименьших значений k, при которых M(k) нельзя представить
# в виде произведения трёх различных натуральных чисел, не равных 1.
# В ответе запишите найденные значения k в порядке возрастания.
def m(k):
    return 7_000_000 + k


def ok(n):
    cnt = 0
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            cnt += 1
        if cnt > 1:
            return False
    if cnt < 2:
        return True
    return False


cnt = 0
for k in range(1, 1000):
    if ok(m(k)):
        print(k)
        cnt += 1
    if cnt == 5:
        break
# 1*3*9*13*21