for x2 in range(100, 1000):
    sx2 = str(x2)
    if len(set(sx2)) == 3:
        x4 = x2 ** 2
        sx4 = str(x4)
        if len(set(sx4)) == 5 and sx4[1] == sx4[-1] and len(set(sx2 + sx4)) == 8:
            print(f'{sx2} * {sx2} = {sx4}')
