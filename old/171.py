# Значение выражения 5 ∙ 729^8 + 7 ∙ 81^12 + 3^16 – 171 записали в системе
# счисления с основанием 9 без незначащих нулей. Сколько чётных цифр
# встречается в этой записи?
n = 5 * 729 ** 8 + 7 * 81 ** 12 + 3 ** 16 - 171
print(n)
cnt = 0
while n:
    d = n % 9
    if d % 2 == 0:
        cnt += 1
    n //= 9
print(cnt)  # 24
