def late(now, classes, bus):
    now_time = str_to_min(now)
    class_time = str_to_min(classes)
    # отфильтровываем афтобусы, на которые не успеем и те на которых доедем с опозданием
    bus = [bus_time for bus_time in bus if bus_time >=
           5 and (now_time + bus_time + 15) <= class_time]
    if not bus:
        return 'Опоздание'
    return f"Выйти через {bus[-1] - 5} минут"  # последний подходящий автобус


def str_to_min(time_str):
    h, m = [int(i) for i in time_str.split(':')]
    return h * 60 + m


def min_to_str(m):
    h = m // 60
    m %= 60
    return f'{h}:{m:02d}'
