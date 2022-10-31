from PIL import Image


def makeanagliph(filename, delta):
    im = Image.open(filename)
    pixels = im.load()
    x, y = im.size
    im2 = Image.new('RGB', (x, y), (255, 255, 255))
    pixels2 = im2.load()
    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            if i - delta >= 0:
                r1, g1, b1 = pixels[i - delta, j]
                pixels2[i, j] = r1, g, b
            else:
                g, b = pixels[i, j][1:]
                pixels2[i, j] = 0, g, b
    im2.save('res.jpg')


makeanagliph("statement-image.jpg", 10)
