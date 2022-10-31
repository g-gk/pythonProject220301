# Ещё немного точек на плоскости
n = int(input())
for i in range(n):
    xy = input().split()
    x, y = map(int, xy)
    if i == 0:
        left, right, top, bottom = (x, y), (x, y), (x, y), (x, y)
    if abs(y) < abs(x):
        print(f'({x}, {y})')
    if x < left[0]:
        left = (x, y)
    if x > right[0]:
        right = (x, y)
    if y < bottom[1]:
        bottom = (x, y)
    if y > top[1]:
        top = (x, y)
print('left:', left)
print('right:', right)
print('top:', top)
print('bottom:', bottom)
