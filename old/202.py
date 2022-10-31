import pymorphy2

i = 99
p = pymorphy2.MorphAnalyzer().parse('бутылка')[0]

while i:
    print('В холодильнике', i, p.make_agree_with_number(i).word, 'кваса.\nВозьмём одну и выпьем.')
    i -= 1
    if i % 10 == 1 and i != 11:
        w = 'Осталась'
    else:
        w = 'Осталось'
    print(w, i, p.make_agree_with_number(i).word, 'кваса.')
