from numpy import array
from numpy import fromiter
from numpy import int8

a = array([1, 4, 10, 34])
print(a)
print(a.dtype)
print(type(a[0]))
print(array([1, 4, 10.324, 34, 'hello']))
print(type(array([1, 4, 10.324, 34, 'hello'])))
print(array(range(10)))
print(fromiter(map(int, '123456789'), dtype=int8))
