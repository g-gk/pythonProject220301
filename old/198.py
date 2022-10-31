def cached(func):
    cache = {}

    def a(*args, **kwargs):
        nonlocal cache
        if not cache.get(args):
            g = func(*args, **kwargs)
            cache[args] = g
            return g
        else:
            return cache[args]

    return a


@cached
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(1000))
