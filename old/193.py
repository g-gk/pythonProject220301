def draw(matrix):
    # вывод поля на экран
    for i in matrix:
        for j in i:
            print(j, end='\t')
        print()


def horizon(matrix):
    # Горизонатльное отражение
    # С помошью функции reversed() выводим каждый элемент в обратном порядке
    for i in matrix:
        for j in reversed(i):
            print(j, end=' ')
        print()


def vertical(matrix):
    # Вертикальное отражение
    # в перевернутой матрице печатаем каждый элемент в правильном порядке
    for i in reversed(matrix):
        for j in i:
            print(j, end=' ')
        print()


def transpose(matrix):
    # с помощью итератора zip() совершаем обход и транспонируем матрицу
    for i in list(zip(*matrix)):
        for j in i:
            print(j, end=' ')
        print()
# transpose([[1, 2, 3], [4, 5, 6]])
# Вывод: 1 4
# 2 5
# 3 6
