print(max(filter(lambda x: x % 3 == 0, [int(input()) for _ in range(3)]), default='Таких чисел нет'))
