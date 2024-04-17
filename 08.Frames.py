from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('New Frame GUI')

frame = LabelFrame(root, text='This is the frame element', padx=5, pady=5)
frame.grid(padx=100, pady=10)

example_button = Button(frame, text='some example button')
example_button.pack(padx=5, pady=5)

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.grid()

root.mainloop()