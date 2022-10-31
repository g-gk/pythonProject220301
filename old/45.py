class Queue:
    def __init__(self, *args):
        a = list()
        for i in args:
            a.append(str(i))
        self.a = a

    def append(self, *args):
        a = self.a
        for i in args:
            a.append(str(i))
        self.a = a

    def __add__(self, other):
        a = self.a
        b = a.copy()
        # print(type(other))
        other = other.s
        otherb = other.copy()
        b.extend(otherb)
        return Queue(*b)

    def __iadd__(self, other):
        a = self.a
        # b = a.copy()
        # print(type(other))
        other = other.s
        # otherb = other.copy()
        a.extend(other)
        return Queue(*a)

    def copy(self):
        a = self.a
        return Queue(*a)

    def pop(self):
        a = []
        if self.a:
            # print(self.a[0])
            a = self.a[0]
            del self.a[0]
        return a if a else None

    def __str__(self):
        a = self.a
        a = ' -> '.join(a)
        return f'[{a}]'

    def extend(self, other):
        a = self.a
        b = other.s
        a.extend(b)

    def next(self):
        return Queue(*self.a[1:])

    def __eq__(self, other):
        if len(self.a) != len(other.s):
            return False
        a = self.a
        b = other.s
        for i in range(len(a)):
            if a[i] != b[i]:
                return False
        return True

    def __rshift__(self, other):
        if self.a:
            return Queue(*self.a[other:])
        return Queue()

    def __iter__(self):
        return self

    def __next__(self):
        return Queue(*self.a[1:])


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
