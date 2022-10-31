from PIL import Image, ImageDraw


def sepulchres(filename, colors, w):
    new_image = Image.new('RGB', (16 * w, 24 * w), colors[0])
    draw = ImageDraw.Draw(new_image)
    draw.ellipse((6 * w, -10 * w, 26 * w, 10 * w), colors[1])
    draw.rectangle((14 * w, 0, 16 * w, w), colors[2])
    draw.rectangle((14 * w, 3 * w, 16 * w, 4 * w), colors[2])
    draw.rectangle((14 * w, 6 * w, 16 * w, 7 * w), colors[2])
    draw.ellipse((4 * w, 0 * w, 28 * w, 24 * w), outline=colors[3], width=w // 5)
    draw.rectangle((0 * w, 12 * w, 16 * w, 24 * w), colors[0])
    draw.ellipse((0 * w, 18 * w, 6 * w, 24 * w), colors[3])
    draw.polygon(((0 * w, 18 * w), (3 * w, 21 * w), (6 * w, 18 * w), (0 * w, 18 * w)), colors[0])
    draw.ellipse((11 * w, 19 * w, 15 * w, 23 * w), colors[4])
    draw.ellipse((8 * w, 16 * w, 12 * w, 20 * w), colors[5])
    draw.ellipse((11 * w, 12 * w, 15 * w, 16 * w), colors[5])
    draw.line((10 * w, 20 * w, 10 * w, 24 * w), fill=colors[6], width=w // 5)
    draw.line((13 * w, 23 * w, 13 * w, 24 * w), fill=colors[6], width=w // 5)
    draw.line((15 * w, 14 * w, 16 * w, 14 * w), fill=colors[6], width=w // 5)
    draw.ellipse((2 * w, 12 * w, 6 * w, 16 * w), colors[7])
    draw.polygon(((0, 13 * w), (0, 14 * w), (2 * w, 14 * w), (0, 13 * w)), colors[8])
    draw.polygon(((6 * w, 14 * w), (8 * w, 14 * w), (8 * w, 13 * w), (6 * w, 14 * w)), colors[8])

    new_image.save(filename)


# col = "#dae3f3", "#0070c0", "#92d050", "#c00000", "#c90", "#ffe699", "#00b050", "#ffc000", "#f6c"
# sepulchres("sepulcarium.png", col, 20)
