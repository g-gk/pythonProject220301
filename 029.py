class Class1:
    def f1(self, *args):
        print('f1')

    def f1(self, *args):
        print('f2')


a = Class1.f1(1)
b = Class1.f1(1, 2)
