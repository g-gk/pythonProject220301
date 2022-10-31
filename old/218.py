import tkinter


def key_pressed(event):
    if event.keysym == 'space':
        canvas.coords(oval, (300, 300, 310, 310))
        canvas.itemconfig(oval, fill='red')
    if event.keysym == 'Up':
        canvas.move(oval, 0, -10)
    if event.keysym == 'Down':
        canvas.move(oval, 0, 10)
    if event.keysym == 'Left':
        canvas.move(oval, -10, 0)
    if event.keysym == 'Right':
        canvas.move(oval, 10, 0)
    if canvas.coords(oval)[1] < 200 or canvas.coords(oval)[1] > 400 \
            or canvas.coords(oval)[2] < 210 or canvas.coords(oval)[2] > 410:
        canvas.itemconfig(oval, fill='green')
    elif canvas.coords(oval)[1] > 200 or canvas.coords(oval)[1] < 400 \
            or canvas.coords(oval)[2] > 210 or canvas.coords(oval)[2] < 410:
        canvas.itemconfig(oval, fill='red')


master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='blue', height=600, width=600)
oval = canvas.create_oval((300, 300), (310, 310), fill='red')
canvas.pack()
master.bind("<KeyPress>", key_pressed)
master.mainloop()
