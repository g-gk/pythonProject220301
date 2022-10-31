import numpy as np

a = np.arange(100)
print(a)
print(a.shape)
b = a.reshape(10, 10)
print(b)
print(b.shape)
c = a.reshape(5, 2, 10)
print(c)
print(c.shape)
