from tkinter import *

root = Tk()

def submit():
    info = entry.get()
    print("heloo", info)

def delete():
    entry.delete(0, END) 

def backspace():
    entry.delete(len(entry.get()) - 1) 
    

entry = Entry(root, font=('Arial', 35), 
              bg='black', fg='green',
              )
entry.pack(side=LEFT)

submit = Button(root, text="Submit", command=submit)
submit.pack(side=LEFT)

delete = Button(root, text="Delete", command=delete)
delete.pack(side=LEFT)

backspace = Button(root, text="Backspace", command=backspace)
backspace.pack(side=LEFT)

root.mainloop()