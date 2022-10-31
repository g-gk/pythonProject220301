# Пограничье
from pprint import pprint


def borderland(*args, **kwargs):
    res = {}
    if 'letter' in kwargs:
        res1 = [arg for arg in args if kwargs['letter'].lower() in arg.lower()]
        if res1:
            res['letter'] = res1
    if 'short' in kwargs:
        res1 = [arg for arg in args if len(arg) <= kwargs['short']]
        if res1:
            res['short'] = res1
    if 'punct' in kwargs:
        if kwargs['punct']:
            res1 = []
            for arg in args:
                flag = False
                for c in arg:
                    if not c.isalpha():
                        flag = True
                        break
                if flag:
                    res1.append(arg)
        else:
            res1 = []
            for arg in args:
                flag = True
                for c in arg:
                    if not c.isalpha():
                        flag = False
                        break
                if flag:
                    res1.append(arg)
        if res1:
            res['punct'] = res1
    for k in res:
        if 'key' in kwargs:
            res[k] = sorted(res[k], key=kwargs['key'])
        else:
            res[k] = sorted(res[k])
    return res


def main():
    print('Пример 1')
    words = [
        "Institute", "Thaumaturgy-VIII", "mainly",
        "octopods", "Alpha", "Centauri-2", "planets"
    ]
    params = {
        "letter": "A",
        "punct": True
    }
    pprint(borderland(*words, **params))

    print('Пример 2')
    words = [
        "Through", "giant", "Glass", "windows",
        "river", "cliffs", "Iowa state", "in the old days"
    ]
    params = {
        "letter": "x",
        "punct": False,
        "short": 5,
        "key": len
    }
    pprint(borderland(*words, **params))


if __name__ == '__main__':
    main()
