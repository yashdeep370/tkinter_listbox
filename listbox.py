from tkinter import *

def add():
    global i
    lbx.insert(ACTIVE,f"{i}")
    i+=1

i=0
root = Tk()
root.geometry("455x233")
root.title("listbox")


lbx = Listbox(root)
lbx.pack()
lbx.insert(END,"FIRST ITEM LISTBOX")
Button(root, text="add item",command=add).pack()

root.mainloop()