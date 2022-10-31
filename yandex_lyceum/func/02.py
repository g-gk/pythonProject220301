# Уравнение прямой
def equation(a, b):
    xa, ya = map(float, a.split(';'))
    xb, yb = map(float, b.split(';'))
    if xa == xb:
        print(xa)
    elif ya == yb:
        print(ya)
    else:
        k = (ya - yb) / (xa - xb)
        b = ya - k * xa
        print(k, b)


def main():
    equation("0;0", "1;1")
    equation("0;0", "0;4")
    equation("4;6.9", "-5.2;6.9")


if __name__ == '__main__':
    main()
