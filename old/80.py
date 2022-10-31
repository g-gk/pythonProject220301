# Инопланетный досуг
from PIL import Image


def hex_to_rgb(s):
    s = s.lstrip("#")
    return tuple([int(s[i:i + 2], 16) for i in range(0, 5, 2)])


def rgb_to_hex(rgb):
    r, g, b = rgb
    return f"#{hex(r)[2:].rjust(2, '0')}" \
           f"{hex(g)[2:].rjust(2, '0')}" \
           f"{hex(b)[2:].rjust(2, '0')}"


def alien_leisure(filename1, filename2, **cols):
    im = Image.open(filename1)
    pixels = im.load()
    x, y = im.size
    for i in range(x):
        for j in range(y):
            if rgb_to_hex(pixels[i, j]) in cols:
                pixels[i, j] = hex_to_rgb(cols[rgb_to_hex(pixels[i, j])])
    im = im.transpose(Image.ROTATE_180)
    im.save(filename2)


def main():
    colors = {
        "#ca86f2": "#a4f957",
        "#585858": "#3a7676",
        "#ffca18": "#f3508d",
        "#b83dba": "#ffacd6"
    }
    alien_leisure("recreation.png", "spare_time.png", **colors)


if __name__ == '__main__':
    main()
