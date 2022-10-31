# В фокусе
from PIL import Image

im = Image.open('image.png')
x, y = im.size
# print(x, y)
pixels = im.load()
x1, y1, x2, y2 = 0, 0, x, y
bg_col = pixels[0, 0]
for i in range(x):
    for j in range(y):
        if pixels[i, j] != bg_col:
            if x1 == 0 or i < x1:
                x1 = i
            if y1 == 0 or j < y1:
                y1 = j
            if x2 == x or i > x2:
                x2 = i
            if y2 == y or j > y2:
                y2 = j
im = im.crop((x1, y1, x2 + 1, y2 + 1))
im.save('res.png')
# im.show()
