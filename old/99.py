from PIL import Image


def makeanagliph(filename, delta):
    # открываем файл
    im1 = Image.open(filename)
    pixels1 = im1.load()  # список с пикселями
    x, y = im1.size  # ширина (x) и высота (y) изображения
    im2 = Image.new('RGB', (x, y), (0, 0, 0))
    pixels2 = im2.load()
    # Пройдем по каждому пикселю в изображении
    for i in range(x):
        for j in range(y):
            if i < delta:
                # Получим для пикселя значение цвета в RGB-нотации
                r, g, b = pixels1[i, j]
                # Присвоим этому пикселю новое значение цвета
                pixels2[i, j] = 0, g, b
            else:
                # Получим для пикселя значение цвета в RGB-нотации
                r, g, b = pixels1[i, j]
                # Делаем сдвиг
                r = pixels1[i - delta, j][0]
                # Присвоим этому пикселю новое значение цвета
                pixels2[i, j] = r, g, b
    # В конце сохраним получившееся изображение с новым именем
    im2.save("res.jpg")