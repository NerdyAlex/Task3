from tkinter import *

root = Tk()
root.title("Simple calculator")
e = Entry(root, width=20, borderwidth=8, fg="Black", bg="grey")
e.pack()
e.insert(0, "guess a number")

def myClick():
    
    hello = "I'm gonna guess your number....\nIs it " + e.get()
    mylabal = Label(root, text=hello)
    mylabal.pack()

botton = Button(root, text="Guess a number", command=myClick, fg="black")
botton.pack()



root.mainloop()