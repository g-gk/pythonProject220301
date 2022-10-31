from math import pi, cos, sin
from PIL import ImageDraw, Image


class MyImageDraw(ImageDraw.ImageDraw):
    def regular_polygon(self, center_coords, sides, radius, rotation=0, fill=None, outline=None):
        x, y = center_coords
        coords = [(x + radius * cos(rotation + 2 * pi * i / sides),
                   y + radius * sin(rotation + 2 * pi * i / sides)) for i in range(1, sides + 1)]
        self.polygon(coords, fill=fill, outline=outline)
