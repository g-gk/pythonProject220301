import tkinter

master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='white', height=600, width=600)
s = 8
l = 600

k = l / s
for i in range(s):
    x = i * k
    canvas.create_line((x, 0), (x, l), fill='black')
    canvas.create_line((0, x), (l, x), fill='black')
canvas.pack()
master.mainloop()
