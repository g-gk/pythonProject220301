# Значение выражения 7 ∙ 729^6 + 6 ∙ 81^9 + 3^14 – 90 записали в системе счисления
# с основанием 9 без незначащих нулей. Сколько чётных цифр встречается
# в этой записи?
n = 7 * 729 ** 6 + 6 * 81 ** 9 + 3 ** 14 - 90
cnt = 0
while n > 0:
    d = n % 9
    if d % 2 == 0:
        cnt += 1
    n //= 9
print(cnt)  # 18
