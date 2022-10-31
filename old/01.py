def print_operation_table(operation, num_rows=9, num_columns=9):
    table = [[0] * num_columns for _ in range(num_rows)]
    for i in range(num_rows):
        for j in range(num_columns):
            table[i][j] = operation(i + 1, j + 1)
    for x in table:
        print(*x, sep='\t')


print_operation_table(lambda x, y: x * y)
