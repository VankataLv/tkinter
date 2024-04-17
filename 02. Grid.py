from tkinter import *

root = Tk()

# Creating a label Widget
myLabel1 = Label(root, text="r:0 - c:0")
myLabel2 = Label(root, text="r:0 - c:1")
myLabel3 = Label(root, text="r:0 - c:2")
myLabel4 = Label(root, text="r:1 - c:0")
myLabel5 = Label(root, text="r:1 - c:1")
myLabel6 = Label(root, text="r:1 - c:2")
myLabel7 = Label(root, text="r:2 - c:0")
myLabel8 = Label(root, text="r:2 - c:1")
myLabel9 = Label(root, text="r:2 - c:2")
myLabel10 = Label(root, text="column 0").grid(row=4, column=0)
myLabel11 = Label(root, text="column 1").grid(row=4, column=1)
myLabel12 = Label(root, text="column 2").grid(row=4, column=2)


# Shoving it onto screen

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=0, column=1)
myLabel3.grid(row=0, column=2)
myLabel4.grid(row=1, column=0)
myLabel5.grid(row=1, column=1)
myLabel6.grid(row=1, column=2)
myLabel7.grid(row=2, column=0)
myLabel8.grid(row=2, column=1)
myLabel9.grid(row=2, column=2)

root.mainloop()
