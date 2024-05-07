from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Demo")
root.geometry('300x150')

def convert():
    global m
    m = entry.get()
    km = m * 1000
    


label = Label(root, text="Meters to kilometers", font="Arial 20 bold",
              )
frame = ttk.Frame(root)
entry = ttk.Entry(frame)
button = ttk.Button(frame, text="Convert", command=convert)

label.pack()
entry.pack(side="left", padx=7)
button.pack(side="left")
frame.pack(padx=3)


output = ttk.Label(root, text="Output", font="Arial 24 bold")
output.pack(padx=3)



root.mainloop()