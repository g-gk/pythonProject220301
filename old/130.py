import tkinter
import random as rd


def draw(event):
    # записываем в 2 переменные рандомные координаты
    first_coordinate = rd.randint(0, 600)
    second_coordinate = rd.randint(0, 600)
    # записысываем рандомный радиус
    radius = rd.randint(1, 600)
    # рисуем круг в рандомном месте рандомного размера
    canvas.create_oval(first_coordinate, second_coordinate,
                       first_coordinate - radius, second_coordinate - radius, fill='red')
    return


master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='blue', height=600, width=600)
canvas.pack()
master.bind("<KeyPress>", draw)
master.mainloop()
