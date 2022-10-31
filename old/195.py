from math import cos, sin, pi

R = 1.0
t_min = 0.0
t_max = 2 * pi
dd = 1e-4
x0 = 0.75
y0 = 0.0


def x(t):
    global R
    return R * cos(t) ** 3


def y(t):
    global R
    return R * sin(t) ** 3


def distance(t):
    global x0
    global y0
    x1 = x(t)
    y1 = y(t)
    return ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5


# оценочное значение шага из руководства
# https://studref.com/543515/matematika_himiya_fizik/metody_minimizatsii_mnogomodalnyh_funktsiy
# пусть начальное значение шага
L = 0.5
step_t = 2 * dd / (L * (t_max - t_min))
# print(step_t)

last_t = t_min  # начинаем с минимального значения t
last_distance = distance(last_t)  # первое найденное значение

min_distance = last_distance
t_for_min_distance = last_t
dd_for_min_distance = 0

while last_t < t_max:  # пока не прошлись по всем возможным значениям
    next_t = last_t + step_t  # следующее текущее значение t
    if next_t > t_max:  # если следующий t больше чем t_max
        next_t = t_max  # t равно t_max
    next_distance = distance(next_t)  # следующее значение расстояния
    # расчитываем разницу расстояний в соседних точках
    current_dd = abs(last_distance - next_distance)
    while current_dd >= dd:  # если шаг лишком крупный
        step_t /= 2  # если шаг лишком крупный уменьшаем шаг
        next_t = last_t + step_t  # следующее текущее значение t
        if next_t > t_max:  # если следующий t больше чем t_max
            next_t = t_max  # t равно t_max
        next_distance = distance(next_t)  # следующее значение расстояния
        # расчитываем разницу расстояний в соседних точках
        current_dd = abs(last_distance - next_distance)

    # обновляем прошлые значения для следующего шага
    last_t = next_t
    last_distance = next_distance

    # обновление данных для минимума если найдено более минимальное расстояние
    if last_distance < min_distance:
        min_distance = last_distance
        t_for_min_distance = last_t
        dd_for_min_distance = current_dd

print(
    f"{min_distance:.3}"
    # f"при t = {t_for_min_distance}, точность расчета {dd_for_min_distance}, шаг = {step_t}."
)
