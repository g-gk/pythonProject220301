# список, который понадобится для склонения слова минута
l_1 = [11, 12, 13, 14, 16, 17, 18, 19]


def late(now, classes, bus):
    # переводим now, classes в минуты
    h_now, m_now = now.split(':')
    now = int(m_now) + int(h_now) * 60
    h_classes, m_classes = classes.split(':')
    classes = int(m_classes) + int(h_classes) * 60
    # рассмротрим минимальное затраченное время, если нам его не хватит, выводим "Опоздание"
    if (now + 20) > classes:
        return 'Опоздание'
    else:
        # создадим переменную status, присвоем ей значение -1
        status = -1
        bus.sort()
        # проходимся по сортированному списку и все подходящие элементы присваеваем status
        for i in range(len(bus)):
            if bus[i] >= 5:

                if not (bus[i] + 15 + now) > classes:
                    status = bus[i]
                else:
                    break
        # если status -1, значит, время ни одно не подходит, а следовательно - опоздание
        if status == -1:
            return 'Опоздание'
        else:
            # теперь рассматриваем status - 5 (т.к. надо еще дойти до остановки)
            # и выбираем подходящий падеж слову 'минута'
            if (status - 5) % 100 not in l_1 and str(status - 5)[-1] == '1':
                return f'Выйти через {status - 5} минуту'
            elif (status - 5) % 100 not in l_1 and str(status - 5)[-1] in '234':
                return f'Выйти через {status - 5} минуты'
            else:
                return f'Выйти через {status - 5} минут'


print(late('12:00', '12:40', [0, 1, 4, 6, 25]))
print(late('9:20', '9:35', [4, 25, 30]))
