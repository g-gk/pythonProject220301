# mapPainter

class Drawer:
    from PIL import Image, ImageDraw

    def __init__(self, draw_map, cell_size):
        self.draw_map = draw_map
        self.cell_size = cell_size
        self.color = {}
        for row in self.draw_map:
            for col in row:
                self.color[col] = 'black'

    def numbers(self):
        res = set()
        for row in self.draw_map:
            for col in row:
                res.add(col)
        return sorted(res)

    def set_color(self, number, color):
        self.color[number] = color

    def set_cell_size(self, cell_size):
        self.cell_size = cell_size

    def size(self):
        if not self.draw_map:
            return 0, 0
        return self.cell_size * len(self.draw_map[0]), self.cell_size * len(self.draw_map)

    def draw(self):
        im = self.Image.new('RGB', self.size(), (0, 0, 0))
        draw = self.ImageDraw.Draw(im)
        k = self.cell_size
        for i in range(len(self.draw_map)):
            for j in range(len(self.draw_map[0])):
                draw.rectangle(((j * k, i * k), ((j + 1) * k, (i + 1) * k)),
                               self.color[self.draw_map[i][j]])
        return im


def main():
    print('----- Пример 1 -----')
    dr = Drawer([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 20)
    cols = {1: 'black', 2: 'red', 3: 'orange', 4: 'yellow', 5: 'green', 6: 'lightblue', 7: 'blue',
            8: 'violet', 9: 'white'}
    for k, v in cols.items():
        dr.set_color(k, v)
    # print(dr.color)
    dr.draw().show()

    print('----- Пример 2 -----')
    # Drawer([[16, 5, 9, 15, 1, 13, 3, 10, 10, 18, 8], [4, 12, 6, 13, 18, 10, 13, 1, 18, 8, 7],
    #         [2, 8, 3, 7, 15, 17, 15, 14, 2, 17, 4], [17, 14, 20, 6, 11, 6, 20, 9, 5, 14, 15],
    #         [9, 13, 7, 7, 5, 9, 18, 15, 5, 2, 20], [19, 15, 4, 12, 7, 18, 14, 14, 13, 18, 15],
    #         [14, 9, 16, 10, 6, 5, 14, 20, 16, 13, 1], [19, 4, 10, 20, 5, 19, 16, 11, 14, 18, 4],
    #         [17, 16, 17, 19, 19, 11, 15, 18, 9, 18, 1], [14, 16, 2, 14, 18, 19, 18, 16, 8, 1, 5],
    #         [17, 15, 13, 12, 19, 1, 13, 11, 15, 13, 13], [16, 18, 15, 14, 12, 14, 19, 10, 9, 1, 20],
    #         [2, 12, 7, 12, 5, 18, 2, 6, 11, 3, 16], [9, 6, 14, 5, 14, 7, 1, 1, 10, 16, 5],
    #         [13, 17, 8, 1, 14, 10, 2, 2, 4, 1, 2], [3, 11, 3, 5, 12, 10, 9, 14, 14, 5, 9],
    #         [12, 1, 20, 13, 12, 4, 11, 15, 13, 1, 11], [3, 8, 13, 11, 9, 19, 13, 18, 7, 9, 9],
    #         [19, 10, 14, 14, 12, 10, 1, 6, 18, 4, 14]], 31).numbers()
    # вернет[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], но
    # было
    # получено[
    #     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 17, 17, 17, 17, 17, 17, 17, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 20, 20, 20, 20, 20, 20, 20]

    print('----- Пример 3 -----')

    print('----- Пример 4 -----')


if __name__ == '__main__':
    main()
