from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('New PIC GUI')
root.iconbitmap("icon_1.ico")

img1 = ImageTk.PhotoImage(Image.open("images/1.jpg"))
img2 = ImageTk.PhotoImage(Image.open("images/2.jpg"))
img3 = ImageTk.PhotoImage(Image.open("images/3.jpg"))

image_list = [img1, img2, img3]
cur_img_index = 0
possible_indexes = set(range(0, len(image_list)))

image_label = Label(image=image_list[cur_img_index])
image_label.grid(row=0, column=1)

status_label = Label(root, text=f'Image {cur_img_index+1} of {len(image_list)}')
status_label.grid(row=2, column=0, columnspan=3, pady=5)

def next_btn():
    global image_label
    global cur_img_index
    global status_label
    if cur_img_index + 1 in possible_indexes:
        cur_img_index += 1
        image_label.grid_forget()
        image_label = Label(image=image_list[cur_img_index])
        image_label.grid(row=0, column=1)
        status_label.grid_forget()
        status_label = Label(root, text=f'Image {cur_img_index + 1} of {len(image_list)}')
        status_label.grid(row=2, column=0, columnspan=3, pady=5)


def back_btn():
    global image_label
    global cur_img_index
    global status_label
    if cur_img_index - 1 in possible_indexes:
        cur_img_index -= 1
        image_label.grid_forget()
        image_label = Label(image=image_list[cur_img_index])
        image_label.grid(row=0, column=1)
        status_label.grid_forget()
        status_label = Label(root, text=f'Image {cur_img_index + 1} of {len(image_list)}')
        status_label.grid(row=2, column=0, columnspan=3, pady=5)


def start_btn():
    global image_label
    global cur_img_index
    global status_label
    cur_img_index = 0
    image_label.grid_forget()
    image_label = Label(image=image_list[cur_img_index])
    image_label.grid(row=0, column=1)
    status_label.grid_forget()
    status_label = Label(root, text=f'Image {cur_img_index + 1} of {len(image_list)}')
    status_label.grid(row=2, column=0, columnspan=3, pady=5)


back_button = Button(root, text="Back", command=back_btn)
back_button.grid(row=1, column=0)

start_button = Button(root, text="Start", command=start_btn)
start_button.grid(row=1, column=1)

next_button = Button(root, text="Next", command=next_btn)
next_button.grid(row=1, column=2)

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.grid(row=3, column=0, columnspan=3)

root.mainloop()