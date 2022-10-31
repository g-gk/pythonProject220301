# Слева направо, сверху вниз
# Даны два числа n и m. Создайте двумерный массив размером n×m и заполните его в
# соответствии с примером.
# Данную задачу необходимо решить с помощью генератора, который заполнит матрицу A.
# Вы должны отправить на проверку единственную строку вида: A = [текст генератора]
n, m = map(int, input().split())
a = [[m * i + j for j in range(m)] for i in range(n)]
for row in a:
    print(*row, sep='\t')
