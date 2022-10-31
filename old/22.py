def bc(variant, user_variant):
    L = min(len(variant), len(user_variant))
    b = 0
    for i in range(L):
        if variant[i] == user_variant[i]:
            b += 1
    c = len(set(variant[:L]) & set(user_variant[:L])) - b
    return b, c


def generate_all_variant():
    var_list = []
    for a in range(9):
        for b in range(9):
            for c in range(9):
                for d in range(9):
                    mn = {a, b, c, d}
                    if len(mn) != 4:
                        continue
                    var_list.append([str(a), str(b), str(c), str(d)])
    return var_list


def get_variants(variants_list, user_variant):
    dic = {}
    for variant in variants_list:
        b, c = bc(variant, user_variant)
        key = (b, c)
        if key in dic:
            dic[key].append(variant)
        else:
            dic[key] = [variant]
    return dic


variants_list = generate_all_variant()
print('Я загадал число. Оно состоит из 4 не повторяющихся цифр.')
print('Попробуйте отгадать')
print('Если число есть но стоит не на своем месте - это Корова.')
print('Если число есть и стоит  на своем месте - это Бык.')
print('Я буду сообщать Вам сколько Быков и Коров в Вашем варианте.')
print('Начнем.')
while True:
    user_variant = []
    while True:
        ch = input('Введите ваш вариант:')
        if ch.isdigit() and len(ch) == 4:
            user_variant = list(ch)
            break
        print('Вы ввели недопустимый вариант.')
    # print(user_variant)
    dic = get_variants(variants_list, user_variant)
    # в словаре ищем самый длинный вариант
    answer_key = None
    MaxLen = 0
    for key, value in dic.items():
        if len(value) > MaxLen:
            answer_key = key
            variants_list = value
            MaxLen = len(value)
    if (answer_key[0] == 4):
        print(f'Ура! Вы отгадали.')
        break
    print(f'Быков: {answer_key[0]}; Коров: {answer_key[1]}')
    # для отладки
    # print(f'Оставшиеся варианты: {variants_list}.')
