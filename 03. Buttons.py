from tkinter import *

root = Tk()


def my_click():
    mylabel = Label(root, text="Look! I clicked a Button")
    mylabel.pack()


#  Creating a button
#  myButton = Button(root, text="Click here!", state=DISABLED) # if state is "DISABLED" u cannot click the button
#  myButton = Button(root, text="Click here!", padx=100, pady=25) # sizes x/y
myButton = Button(root, text="Click here!", command=my_click)  # what to do when click
myButton2 = Button(root, text="Click here!", command=my_click, padx=100, pady=25, bg="red", fg="black")  # what to do when click

myButton.pack()
myButton2.pack()
root.mainloop()
