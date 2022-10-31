original = print


def print(*args, **kwargs):
    args = (i.upper() if isinstance(i, str) else i for i in args)
    original(*args, **kwargs)


print('Нельзя ли потише?')
