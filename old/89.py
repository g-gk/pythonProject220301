from PIL import Image, ImageDraw

im = Image.new('RGB', (500, 300), (255, 255, 255))
draw = ImageDraw.Draw(im)

draw.line((10, 200, 60, 100), fill='pink', width=15)
draw.line((10, 100, 10, 200), fill='pink', width=15)
draw.line((60, 100, 60, 200), fill='pink', width=15)

draw.line((100, 100, 90, 200), fill='pink', width=15)
draw.line((90, 100, 140, 200), fill='pink', width=15)

draw.line((180, 100, 180, 200), fill='pink', width=20)
draw.ellipse((180, 140, 230, 200), fill='pink')

draw.line((250, 150, 300, 150), fill='pink', width=15)
draw.line((250, 100, 250, 200), fill='pink', width=15)
draw.line((300, 100, 300, 200), fill='pink', width=15)

draw.line((330, 100, 350, 170), fill='pink', width=13)
draw.line((380, 100, 330, 200), fill='pink', width=15)

draw.ellipse((410, 100, 465, 160), fill='pink')
draw.line((410, 100, 410, 200), fill='pink', width=15)

im.save('draw-ellipse-rectangle-line.jpg', quality=95)
im.show()
