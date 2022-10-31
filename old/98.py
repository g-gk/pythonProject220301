from PIL import Image, ImageDraw
from math import sin, cos, pi


class MyImageDraw(ImageDraw.ImageDraw):
    def __init__(self, im, mode=None):
        ImageDraw.ImageDraw.__init__(self, im, mode)

    def regular_polygon(self, center_coords, sides, radius, rotation=0, fill=None, outline=None):
        corn = rotation
        step_corn = 2 * pi / sides
        coords = []
        for i in range(sides):  # цикл по числу сторон
            x = radius * cos(corn) + center_coords[0]
            y = radius * sin(corn) + center_coords[1]
            coords.append((x, y))
            corn += step_corn
        self.polygon(coords, fill, outline)


im = Image.new('RGB', (800, 600))
draw = MyImageDraw(im)
draw.ellipse((200, 200), 50, fill='#00FFFF', outline="#FF00FF", width=5)
draw.regular_polygon((400, 400), 5, 100, fill='#FF00FF', outline='#00FFFF')
im.save('res.jpg')
im.show()
