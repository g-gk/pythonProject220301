# Польский калькулятор — 2
from math import factorial

stack = []
com = input().split()
for c in com:
    if c.isdigit() or c[1:].isdigit():
        stack.append(int(c))
    elif c == '+':
        stack.append(stack.pop() + stack.pop())
    elif c == '*':
        stack.append(stack.pop() * stack.pop())
    elif c == '-':
        stack.append(- stack.pop() + stack.pop())
    elif c == '/':
        x = stack.pop()
        stack.append(stack.pop() // x)
    elif c == '!':
        stack.append(factorial(stack.pop()))
    elif c == '#':
        stack.append(stack[-1])
    elif c == '~':
        stack.append(-stack.pop())
    elif c == '@':
        x3, x2, x1 = stack.pop(), stack.pop(), stack.pop()
        stack += [x2, x3, x1]
print(*stack)
