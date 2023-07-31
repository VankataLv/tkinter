from tkinter import *
root = Tk()
root.title("Basic Calculator")

field = Entry(root, width=60, bg="white", fg="black", borderwidth=5)
field.grid(row=5, column=0, columnspan=4, padx=20, pady=40)
# field.insert(0, "Write your name!")     # default text in the input box


def button_click(number):
    # field.delete(0, END) # delete the box
    current_num = field.get()
    field.delete(0, END)
    field.insert(0, str(current_num) + str(number))


def button_clear():
    field.delete(0, END)


def button_add():
    first_num = field.get()
    global f_num
    global action
    action = "add"
    f_num = int(first_num)
    field.delete(0, END)


def button_equal():
    second_num = field.get()
    field.delete(0, END)
    if action == "add":
        field.insert(0, str(f_num + int(second_num)))
    elif action == "subtract":
        field.insert(0, str(f_num - int(second_num)))
    elif action == "multiply":
        field.insert(0, str(f_num * int(second_num)))
    elif action == "divide":
        field.insert(0, str(f_num / int(second_num)))


def button_subtract():
    first_num = field.get()
    global f_num
    global action
    action = "subtract"
    f_num = int(first_num)
    field.delete(0, END)


def button_multiply():
    first_num = field.get()
    global f_num
    global action
    action = "multiply"
    f_num = int(first_num)
    field.delete(0, END)


def button_divide():
    first_num = field.get()
    global f_num
    global action
    action = "divide"
    f_num = int(first_num)
    field.delete(0, END)


button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7), bg="thistle1", font=40)
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8), bg="thistle1", font=40)
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9), bg="thistle1", font=40)
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4), bg="thistle1", font=40)
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5), bg="thistle1", font=40)
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6), bg="thistle1", font=40)
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1), bg="thistle1", font=40)
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2), bg="thistle1", font=40)
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3), bg="thistle1", font=40)
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0), bg="thistle1", font=40)
button_add = Button(root, text="+", padx=37, pady=20, command=button_add, bg="yellow", font=40)
button_subtract = Button(root, text="-", padx=39, pady=20, command=button_subtract, bg="green", font=40)
button_multiply = Button(root, text="x", padx=38, pady=20, command=button_multiply, bg="grey", font=40)
button_divide = Button(root, text="/", padx=39, pady=20, command=button_divide, bg="white", font=40)
button_equal = Button(root, text="=", padx=141, pady=20, command=button_equal, bg="DeepSkyBlue1", font=40)
button_clear = Button(root, text="C", padx=39, pady=20, command=button_clear, bg="red", font=40)
# button_pos_neg = Button(root, text="+/-", padx=36, pady=20, command=button_click("+"), bg='tan1', font=40)
# button_float = Button(root, text=",", padx=42, pady=20, command=button_click("+"), bg="lawn green", font=40)

button_7.grid(row=0, column=0)
button_8.grid(row=0, column=1)
button_9.grid(row=0, column=2)
button_divide.grid(row=0, column=3)
button_4.grid(row=1, column=0)
button_5.grid(row=1, column=1)
button_6.grid(row=1, column=2)
button_multiply.grid(row=1, column=3)
button_1.grid(row=2, column=0)
button_2.grid(row=2, column=1)
button_3.grid(row=2, column=2)
button_subtract.grid(row=2, column=3)
button_0.grid(row=3, column=0)
# button_pos_neg.grid(row=3, column=1)
# button_float.grid(row=3, column=2)
button_add.grid(row=3, column=3)
button_clear.grid(row=4, column=0)
button_equal.grid(row=4, column=1, columnspan=3)


root.mainloop()
