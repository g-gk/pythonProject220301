class A:
    def __str__(self):
        return 'A.__str__ method'

    def hello(self):
        print('Hello')


class B:
    def __str__(self):
        return 'B.__str__ method'

    def good_evening(self):
        print('Good evening')


class C(A, B):
    def __str__(self):
        return A.__str__(self)


class D(A, B):
    def __str__(self):
        return B.__str__(self)


c = C()
c.hello()
c.good_evening()
d = D()
d.hello()
d.good_evening()
print(c)
print(d)
