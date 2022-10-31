# Правильная скобочная последовательность
def bracket_check(test_string):
    stack = []
    for c in test_string:
        if c == '(':
            stack += [c]
        elif c == ')':
            if stack:
                stack.pop()
            else:
                print('NO')
                return None
    if stack:
        print('NO')
    else:
        print('YES')


def main():
    bracket_check("()")
    bracket_check("(()((")


if __name__ == '__main__':
    main()
