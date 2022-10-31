def late(now, classes, bus):
    now = now.split(':')
    now[0], now[-1] = int(now[0]), int(now[-1])
    now1 = now[0] * 60 + now[-1]
    classes = classes.split(':')
    classes[0], classes[-1] = int(classes[0]), int(classes[-1])
    classes1 = (classes[0] * 60 + classes[-1]) - now1
    ans = []
    for time in bus:
        if time >= 5 and time <= classes1 - 15:
            ans.append(time)
    if ans == []:
        return 'Опоздание'
    else:
        return 'Выйти через ' + str(max(ans) - 5) + ' минут'


print(late('12:00', '12:40', [0, 1, 4, 6, 25]))
print(late('9:20', '9:35', [4, 25, 30]))
