from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('New PIC GUI')
root.iconbitmap("C:/Users/Ivan Lilov/Desktop/GitHub/tkinter/tkinter/icon_1.ico")

# my_image = ImageTk.PhotoImage(Image.open("C:/Users/Ivan Lilov/Desktop/GitHub/tkinter/tkinter/car.png"))
my_image2 = ImageTk.PhotoImage(Image.open("car.png"))
# my_label = Label(image=my_image)
image_label = Label(image=my_image2)
image_label.pack()
# my_label.pack()
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()
root.mainloop()
