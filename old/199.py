def cached(func):
    res_dict = {}

    def wrapped(*args, **kwargs):
        nonlocal res_dict
        key1 = ','.join([str(i) for i in args])
        key2 = ','.join([str(key) + '=' + str(value)
                         for key, value in kwargs.items()])
        key = f'({key1}),({key2})'
        if key not in res_dict:
            res_dict[key] = func(*args, **kwargs)
            # print(f'Ключ: {key}, значение вычислено {res_dict[key]}')
        # else:
        # print(f'Ключ: {key}, значение взято из ранее вычисленных {res_dict[key]}')
        return res_dict[key]

    return wrapped


@cached
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# for i in range(1, 10):
#     print(fib(i))
#
# for i in range(1, 10):
#     print(fib(i))
print(fib(100))
