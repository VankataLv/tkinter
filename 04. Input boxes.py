from tkinter import *

root = Tk()

e = Entry(root, width=50, bg="pink", fg="black", borderwidth=5)
e.pack()
e.insert(0, "Write your name!")     # default text in the input box

def my_click():
    mylabel = Label(root, text='Hello ' + e.get())
    mylabel.pack()


myButton = Button(root, text="Enter", command=my_click)
myButton.pack()

root.mainloop()
