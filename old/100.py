from PIL import Image, ImageDraw

# создание изображения
im = Image.new("RGB", (1050, 300), (0, 0, 0))
# на изображении создаем рисунок для рисования
draw = ImageDraw.Draw(im)
# рисуем букву а
draw.line((50, 150, 150, 150), '#ffc801', width=18)
draw.line((100, 0, 0, 300), '#ff0800', width=10)
draw.line((100, 0, 200, 300), '#fe9a00', width=15)
# рисуем букву м
draw.line((275, 0, 375, 150), '#d2ff01', width=10)
draw.line((375, 150, 475, 0), '#d2ff01', width=10)
for i in range(0, 300, 50):
    draw.ellipse(((250, i), (300, i + 50)), '#f7ff00')
    draw.ellipse(((450, i), (500, i + 50)), '#89ff01')
# рисуем букву и
draw.line((550, 0, 550, 300), '#10ff94', width=15)
draw.line((700, 0, 700, 300), '#00CED1', width=15)
draw.line((550, 300, 700, 0), '#00FFFF', width=15)
# рисуем буква р
draw.line((750, 0, 750, 300), '#00BFFF', width=15)
draw.line((765, 0, 765, 300), '#1E90FF', width=15)
draw.arc(((700, 0), (850, 150)), -90, 90, '#0000CD', 25)
# рисуем букву а
draw.line((900, 150, 1000, 150), '#8A2BE2', width=18)
draw.line((950, 0, 850, 300), '#9932CC', width=10)
draw.line((950, 0, 1050, 300), '#4B0082', width=15)
# сохранаям изображение
im.save('name.png')
im.show()
