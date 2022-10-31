# Пятнашки
from PIL import Image

im = Image.open('image.bmp')
x, y = im.size
kx, ky = x // 4, y // 4
for i in range(4):
    for j in range(4):
        if i + j != 6:
            im1 = im.copy()
            im1.crop((i * kx, j * ky, (i + 1) * kx, (j + 1) * ky))
            im1.save(f'image{j + 1}{i + 1}.bmp')
