food = {'жирное': ["растительное масло", "сало", "майонез", "бургер", "свиной смалец"],
        'сладкое': ['шоколад', 'пончики', 'мороженое', 'вафли', 'печенье', 'мёд', 'сахар', 'торт'],
        'мучное': ["печенье", "пирожки", "булки", "пончики"],
        'диетическое': ['творог', 'фрукты', 'каша', 'зелень', 'овощи', 'чай', 'ягоды', 'рис']}


def diet(foods):
    # переменная, которая считает диетическую еду
    ch = 0
    foods = foods.split(', ')
    # проходимся по всей еде, увеличиваем счетчик, когда встречаем что-то диетическое
    for i in range(len(foods)):
        if foods[i] in food['диетическое']:
            ch += 1
    # если больше половины блюд не относятся к диетическим, выводим "Не ешь столько, По!"
    if ch < (len(foods) / 2):
        return 'Не ешь столько, По!'
    # в обратном случае "Так держать, Воин Дракона!"
    else:
        return 'Так держать, Воин Дракона!'


print(diet("творог"))
print(diet("печенье, чай, сахар, фрукты, мед"))
