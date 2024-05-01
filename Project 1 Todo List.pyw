import tkinter as tk
from tkinter import ttk
from tkinter import *


def creat():
    root2 = Tk()

    def add():
        t = " "
        t = e1.get()
        print(t)
        listBox.insert(END, t)
        root2.destroy()

    # This is the section of code which creates the main window
    root2.geometry('560x130')
    root2.configure(background='#FFF4BB')
    root2.title('Add Task')

    # This is the section of code which creates a button
    Button(root2, text='Add', bg='#F7D460', font=('arial', 12, 'italic'), command=add).place(x=250, y=78)

    # This is the section of code which creates a text input box
    e1 = Entry(root2)
    e1.place(x=202, y=34)
    

    # This is the section of code which creates the a label
    Label(root2, text='Please Add task to the List', bg='#FFF4BB', font=('courier', 12, 'normal')).place(x=142, y=8)

    root2.mainloop()






# this is the function called when the button is clicked
def delete():
    listBox.delete(listBox.curselection())




root = Tk()

# This is the section of code which creates the main window
root.geometry('500x500')
root.configure(background='#FFF4BB')
root.title('ToDo')


# This is the section of code which creates a button
Button(root, text='Create', bg='#F7D460', font=('arial', 12, 'italic'), command=creat).place(x=100, y=400)


# This is the section of code which creates a listbox
listBox=Listbox(root, bg='white', font=('arial', 12, 'normal'), width=35, height=16)
listBox.place(x=40, y=20)


# This is the section of code which creates a button
Button(root, text='Delete', bg='#F7D460', font=('arial', 12, 'italic'), command=delete).place(x=350, y=400)


root.mainloop()
