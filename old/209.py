from tkinter import *
from math import *

n = 5
w, h = 800, 600
radius = w / 4
x0, y0 = w / 2, h / 2
alpha = 2 * pi / n

root = Tk()
kanva = Canvas(root, width=w, height=h, bg="white")
kanva.pack()
for k in range(n):
    kanva.create_line(x0 + radius * cos(k * alpha),
                      y0 + radius * sin(k * alpha),
                      x0 + radius * cos((k + 2) * alpha),
                      y0 + radius * sin((k + 2) * alpha)
                      )
root.mainloop()
