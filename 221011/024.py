def imp(a, b):
    return not a or b


print('x y z w f')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                f = (imp(x, y) and imp(y, w)) or (z == (x or y))
                if not f:
                    print(x, y, z, w, int(f))
