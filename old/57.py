class Queue:
    def __init__(self, *args):
        self.q = []
        if len(args) > 0:
            self.q = [*args]

    def append(self, *values):
        self.q += [*values]

    def copy(self):
        return Queue(*self.q)

    def pop(self):
        if not self.q:
            return None
        res = self.q[0]
        self.q = self.q[1:]
        return res

    def extend(self, queue):
        self.q += queue.q

    def next(self):
        if len(self.q) < 1:
            return Queue()
        return Queue(*self.q[1:])

    def __add__(self, other):
        return Queue(*(self.q + other.q))

    def __iadd__(self, y):
        self.q += y.q
        return self

    def __eq__(self, y):
        return self.q == y.q

    def __rshift__(self, N):
        if N > len(self.q):
            return Queue()
        return Queue(*self.q[N:])

    def __str__(self):
        s = ' -> '.join([str(i) for i in self.q])
        return f'[{s}]'

    def __next__(self):
        return self.next()


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
