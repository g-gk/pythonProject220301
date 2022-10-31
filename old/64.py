# класс A
class A:
    # возвращает 'A.__str__ method
    def __str__(self):
        return 'A.__str__ method'

    # выводит на экран строку 'Hello'
    def hello(self):
        print('Hello')


# класс B
class B:
    # возвращает 'B.__str__ method
    def __str__(self):
        return 'B.__str__ method'

    # выводит на экран строку 'Good evening'
    def good_evening(self):
        print('Good evening')


# клас C, унаследованный от A и B
class C(A, B):
    # используем метод базового класса A
    def __str__(self):
        return A.__str__(self)


# клас D, унаследованный от A и B
class D(A, B):
    # используем метод базового класса B
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
