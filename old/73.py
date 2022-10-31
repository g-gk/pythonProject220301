def print_board():
    print('     +----+----+----+----+----+----+----+----+')
    for row in range(7, -1, -1):
        print(' ', row, end='  ')
        for col in range(8):
            print('|', '  ', end=' ')
        print('|')
        print('     +----+----+----+----+----+----+----+----+')
    print(end='       ')
    for col in range(8):
        print(col, end='    ')
    print()


print_board()
