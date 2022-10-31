import tkinter

size = 600
lenn = 8

master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='black', height=600, width=600)

for i in range(1, lenn):
    x = i * size / lenn
    canvas.create_line((x, 0), (x, size), fill='white')
    canvas.create_line((0, x), (size, x), fill='white')

canvas.create_oval((0, 0), (75, 75), fill='red')
canvas.create_oval((150, 150), (75, 75), fill='red')

canvas.create_oval((225, 0), (150, 75), fill='red')
canvas.create_oval((0, 225), (75, 150), fill='red')

canvas.create_oval((225, 225), (150, 150), fill='red')
canvas.create_oval((300, 150), (225, 75), fill='red')

canvas.create_oval((375, 0), (300, 75), fill='red')
canvas.create_oval((375, 225), (300, 150), fill='red')

canvas.create_oval((450, 150), (375, 75), fill='red')
canvas.create_oval((525, 0), (450, 75), fill='red')

canvas.create_oval((525, 225), (450, 150), fill='red')
canvas.create_oval((600, 150), (525, 75), fill='red')

canvas.create_oval((0, 525), (75, 450), fill='white')
canvas.create_oval((75, 450), (150, 375), fill='white')

canvas.create_oval((75, 600), (150, 525), fill='white')
canvas.create_oval((225, 525), (150, 450), fill='white')

canvas.create_oval((300, 450), (225, 375), fill='white')
canvas.create_oval((300, 600), (225, 525), fill='white')

canvas.create_oval((375, 525), (300, 450), fill='white')
canvas.create_oval((450, 450), (375, 375), fill='white')

canvas.create_oval((450, 600), (375, 525), fill='white')
canvas.create_oval((525, 525), (450, 450), fill='white')

canvas.create_oval((600, 600), (525, 525), fill='white')
canvas.create_oval((600, 450), (525, 375), fill='white')
canvas.pack()
master.mainloop()
