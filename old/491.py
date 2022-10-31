# Очередь и все-все-все

class Queue:
    def __init__(self, *args):
        self.args = list(args)

    def append(self, *values):
        self.args += values

    def copy(self):
        return Queue(*self.args[::])

    def pop(self):
        if self.args:
            return self.args.pop(0)

    def extend(self, other):
        self.args += other.args

    def next(self):
        return Queue(*self.args[1:])

    def __str__(self):
        return f'[{" -> ".join(map(str, self.args))}]'

    def __eq__(self, other):
        return self.args == other.args

    def __add__(self, other):
        return Queue(*(self.args + other.args))

    def __iadd__(self, other):
        self.args += other.args
        return self

    def __rshift__(self, n):
        return Queue(*self.args[n:])

    def __next__(self):
        return self.next()


def main():
    print('----- Пример 1 -----')
    q1 = Queue(1, 2, 3)
    print(q1)
    q1.append(4, 5)
    print(q1)
    qx = q1.copy()
    print(qx.pop())
    print(qx)
    q2 = q1.copy()
    print(q2)
    print(q1 == q2, id(q1) == id(q2))
    q3 = q2.next()
    print(q1, q2, q3, sep='\n')
    print(q1 + q3)
    q3.extend(Queue(1, 2))
    print(q3)
    q4 = Queue(1, 2)
    q4 += q3 >> 4
    print(q4)
    q5 = next(q4)
    print(q4)
    print(q5)

    print('----- Пример 2 -----')
    q1 = Queue(*range(1, 5))
    print(q1)
    q1.append(*range(5, 7))
    print(q1)
    q2 = q1 >> 3
    print(q1)
    print(q2)
    q3 = q1 >> 20
    print(q3)
    q4 = q1
    q1 += q2
    print(q1)
    print(q4)
    print(q1 + q4)

    print('----- Пример 3 -----')

    print('----- Пример 4 -----')


if __name__ == '__main__':
    main()
