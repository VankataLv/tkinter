from tkinter import *

root = Tk()

option_clicked = IntVar()

def option_clicked_func(value_clicked):
    option_label = Label(root, text=value_clicked)
    option_label.pack()


Radiobutton(root, text='option 1', variable=option_clicked, value=1, command=lambda: option_clicked_func(option_clicked.get())).pack()
Radiobutton(root, text='option 2', variable=option_clicked, value=2, command=lambda: option_clicked_func(option_clicked.get())).pack()
Radiobutton(root, text='option 3', variable=option_clicked, value=3, command=lambda: option_clicked_func(option_clicked.get())).pack()

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()


mainloop()