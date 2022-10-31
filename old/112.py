from timeit import timeit

print(timeit("[sqrt(x) for x in range(10_000_000)]",
             "from math import sqrt", number=1))

print(timeit("for i in range(10_000_000): a.append(sqrt(i))",
             "from math import sqrt; a=[]", number=1))

print(timeit("list(map(sqrt, range(10_000_000)))",
             "from math import sqrt", number=1))

print(timeit("list(map(lambda x: x**0.5, range(10_000_000)))",
             "from math import sqrt", number=1))

# 1.1052031
# 1.2499985999999998
# 0.9432386999999998
# 2.0043206000000002
