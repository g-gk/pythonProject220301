class A:
    pass


class B(A):
    pass


class BaseC:
    def bar(self):
        print('bar')


class C(BaseC):
    def foo(self):
        print('foo')


c = C()
c.foo()
c.bar()
c.baz()
