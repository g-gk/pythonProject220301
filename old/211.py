import tkinter
import random
from random import randint


def draw(event):
    canvas.create_oval((random.randint(1, 100), random.randint(1, 100)),
                       (random.randint(1, 300), random.randint(1, 300)), fill='red')

    return


master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='blue', height=600, width=600)
canvas.pack()
master.bind("<Button-1>", draw)
master.mainloop()
