import tkinter


def show_key(event):
    text = ', '.join(map(str, [event.keysym, event.char, event.keysym_num, event.keycode]))
    label.config(text=text)


master = tkinter.Tk()
label = tkinter.Label(master, text="Hello world!")
label.pack()
master.bind("<KeyPress>", show_key)
master.mainloop()
